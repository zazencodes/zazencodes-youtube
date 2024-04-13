from meal_demand.dataprep.prep_load import prep_load
from meal_demand.dataprep.prep_filter import prep_filter
from meal_demand.dataprep.prep_ohe import prep_ohe
from meal_demand.feateng.feat_ts import feat_ts
from meal_demand.domain.config import Config
from meal_demand.ml.train import train

import os
from uuid import uuid4
from pathlib import Path

DATA_PATH = os.getenv("DATA_PATH")
if not DATA_PATH:
    raise RuntimeError("DATA_PATH env variable not set. Exiting.")

MODELS_PATH = os.getenv("MODELS_PATH")
if not MODELS_PATH:
    raise RuntimeError("MODELS_PATH env variable not set. Exiting.")

model_id = uuid4().hex[:5]
print(f"Starting model training: model_id={model_id}")

config = Config(
    data_path=Path(DATA_PATH),
    models_path=Path(MODELS_PATH),
    model_id=model_id,
    model_params={
        "n_estimators": 1000,
        "max_depth": 5,
        "learning_rate": 0.01,
        "loss": "squared_error",
        "validation_fraction": 0.05,
        "n_iter_no_change": 15,
        "verbose": 1,
    },
    fulfilment_center_file="kaggle/fulfilment_center_info.csv",
    meal_info_file="kaggle/meal_info.csv",
    train_file="kaggle/train.csv",
    target="num_orders",
    numeric_features=[
        "checkout_price",
        "base_price",
        "emailer_for_promotion",
        "homepage_featured",
        "num_orders_shift_1",
        "num_orders_shift_52",
        "num_orders_rolling_4",
        "num_orders_rolling_16",
        "num_orders_rolling_4_shift_52",
        "num_orders_rolling_16_shift_52",
    ],
    ohe_features=[
        "city_code",
        "region_code",
        "center_type",
        "op_area",
        "category",
        "cuisine",
    ],
)

df = prep_load(config)
df = feat_ts(df)
df, ohe_processed_features = prep_ohe(df, config)
feature_columns = [config.target] + config.numeric_features + ohe_processed_features
df = prep_filter(df)
train(df, feature_columns, config)

print(f"Completed model training: model_id={model_id}")
