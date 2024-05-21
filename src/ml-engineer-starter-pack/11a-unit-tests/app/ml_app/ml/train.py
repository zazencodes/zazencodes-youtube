from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from joblib import dump
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error

from ..config import FEATURE_COLUMNS, MODEL_PARAMS, MODEL_PATH, TARGET_COLUMN
from ..utils.common import get_logger

logger = get_logger()


def train(df: pd.DataFrame, model_id: str):
    """
    Train and save model.
    """
    logger.info(f"Started train")
    reg = _train(df, FEATURE_COLUMNS, TARGET_COLUMN, MODEL_PARAMS)
    mse = _get_traning_mertrics(reg, df, FEATURE_COLUMNS, TARGET_COLUMN)
    logger.info(f"Training metrics: mse={mse}")
    _store_model(reg, MODEL_PATH, model_id)
    logger.info(f"Completed train")
    return df


def _train(
    df: pd.DataFrame,
    feature_columns: List[str],
    target_column: str,
    model_params: dict,
) -> HistGradientBoostingRegressor:
    X = df[feature_columns].values
    y = df[target_column].values
    reg = HistGradientBoostingRegressor(**model_params)
    reg.fit(X, y)
    return reg


def _get_traning_mertrics(
    reg: HistGradientBoostingRegressor,
    df: pd.DataFrame,
    feature_columns: List[str],
    target_column: str,
) -> float:
    X = df[feature_columns].values
    y = df[target_column].values
    y_pred = reg.predict(X)
    mse = np.sqrt(mean_squared_error(y, y_pred))
    return mse


def _store_model(reg: HistGradientBoostingRegressor, model_path: Path, model_id: str):
    name = "gbr"
    fp = model_path / f"{name}_{model_id}.pkl"
    dump(reg, fp)
    logger.info(f"Stored model: file={str(fp)}")
