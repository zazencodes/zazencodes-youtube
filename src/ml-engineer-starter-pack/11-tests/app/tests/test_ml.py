# import sys
#
# sys.path.append("../")

from pathlib import Path

import pandas as pd
import numpy as np
import pytest
from joblib import load
from sklearn.exceptions import NotFittedError

from ml_app.config import FEATURE_COLUMNS, MODEL_PARAMS, TARGET_COLUMN
from ml_app.ml.predict import _predict
from ml_app.ml.train import _get_traning_mertrics, _train

TRAIN_DATA_FILE = "../../data/pytest_ml_train.Video_Games_Sales_as_at_22_Dec_2016.csv"
MODEL_PATH = "models/gbr_abiwh28.pkl"
PRED_DATA_FILE = "../../data/pytest_ml_pred.Video_Games_Sales_as_at_22_Dec_2016.csv"
PRED_DATA_LENGTH = 7
MAX_PRED_VALUE = 10000

MAX_MSE = 2


def test_train():
    df = pd.read_csv(TRAIN_DATA_FILE)
    reg = _train(df, FEATURE_COLUMNS, TARGET_COLUMN, MODEL_PARAMS)
    try:
        reg.predict(df[FEATURE_COLUMNS].values[:5])
    except NotFittedError:
        raise


def test_get_traning_mertrics():
    reg = load(MODEL_PATH)
    df = pd.read_csv(TRAIN_DATA_FILE)
    mse = _get_traning_mertrics(reg, df, FEATURE_COLUMNS, TARGET_COLUMN)

    # Error is numeric
    assert type(mse) == np.float64

    # Error is within expected range
    assert 0 < mse < MAX_MSE


# TODO: fix
# def test_predict():
#     reg = load(MODEL_PATH)
#     df = pd.read_csv(PRED_DATA_FILE)
#     y_pred = _predict(reg, df, FEATURE_COLUMNS)
#
#     # Correct number of predictions
#     assert len(y_pred) == PRED_DATA_LENGTH
#
#     # Predictions have proper type
#     assert all((type(y) == np.float64 for y in y_pred))
#
#     # Precitions are in proper range
#     assert all((0 < y < MAX_PRED_VALUE for y in y_pred))
