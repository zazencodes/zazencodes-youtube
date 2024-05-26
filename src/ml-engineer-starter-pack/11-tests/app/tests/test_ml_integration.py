# import sys
#
# sys.path.append("../")

from pathlib import Path

import pandas as pd
import numpy as np
import pytest

from ml_app.config import ID_COLUMNS, TARGET_COLUMN
from ml_app.ml.predict import predict
from ml_app.ml.train import train
from ml_app.dataprep.prep_filter import prep_filter
from ml_app.dataprep.prep_load import prep_load
from ml_app.feateng.feat_bin import feat_bin

TRAIN_DATA_FILE = "../../data/train.Video_Games_Sales_as_at_22_Dec_2016.csv"
PRED_DATA_FILE = "../../data/pred.Video_Games_Sales_as_at_22_Dec_2016.csv"

MODEL_ID = "abiwh28"
MODEL_OUTPUT_FILE = "models/gbr_{model_id}.pkl"
PREDICTION_OUTPUT_FILE = "predictions/gbr_{model_id}.csv"

PRED_DATA_LENGTH = 7

SEED = 18


def test_train():

    model_output_file = Path(MODEL_OUTPUT_FILE.format(model_id=MODEL_ID))
    model_output_file.unlink(missing_ok=True)

    np.random.seed(SEED)
    df = prep_load(Path(TRAIN_DATA_FILE))
    df = prep_filter(df)
    df = feat_bin(df)
    train(df, MODEL_ID)

    # Model was saved
    assert model_output_file.exists()


def test_predict():

    prediction_output_file = Path(PREDICTION_OUTPUT_FILE.format(model_id=MODEL_ID))
    prediction_output_file.unlink(missing_ok=True)

    df = prep_load(Path(PRED_DATA_FILE))
    df = prep_filter(df, for_pred=True)
    df = feat_bin(df)
    predict(df, MODEL_ID)

    # Predictions were saved
    assert prediction_output_file.exists()

    df_pred = pd.read_csv(prediction_output_file)

    # Predictions have proper length
    assert len(df_pred) == PRED_DATA_LENGTH

    # Predictions have proper columns
    assert f"Pred_{TARGET_COLUMN}" in df_pred.columns
    assert all((col in df_pred.columns for col in ID_COLUMNS))
