from meal_demand.domain.config import Config
from meal_demand.dataprep.prep_load import prep_load
from meal_demand.dataprep.prep_filter import prep_filter
from meal_demand.dataprep.prep_ohe import prep_ohe
from meal_demand.feateng.feat_ts import feat_ts
from meal_demand.domain.config import Config
from meal_demand.ml.predict import predict

import numpy as np
import os
from uuid import uuid4
from pathlib import Path

DATA_PATH = os.getenv("DATA_PATH")
if not DATA_PATH:
    raise RuntimeError("DATA_PATH env variable not set. Exiting.")

MODELS_PATH = os.getenv("MODELS_PATH")
if not MODELS_PATH:
    raise RuntimeError("MODELS_PATH env variable not set. Exiting.")

MODEL_ID = os.getenv("MODEL_ID")
if not MODEL_ID:
    raise RuntimeError("MODEL_ID env variable not set. Exiting.")


CENTER_TYPE = os.getenv("CENTER_TYPE")


# meal-demand predict.py --center-id=177 --meal-id=1445

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--center-id", help="The center id to predict demand for")
parser.add_argument("--meal-id", help="The meal id to predict demand for")
args = parser.parse_args()


print(f"Starting predict: model_id={MODEL_ID}")


config = Config(
    seed=None,
    data_path=Path(DATA_PATH),
    models_path=Path(MODELS_PATH),
    center_type=CENTER_TYPE,
    model_params=None,
    model_id=MODEL_ID,
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
    max_week=145,
)


print(f"Completed prediction: model_id={MODEL_ID}")


np.random.seed(config.seed)
df = prep_load(config)
df = feat_ts(df)
df, ohe_processed_features = prep_ohe(df, config)
feature_columns = [config.target] + config.numeric_features + ohe_processed_features
df = prep_filter(df)
predict(df, feature_columns, config, args.center_id, args.meal_id)
