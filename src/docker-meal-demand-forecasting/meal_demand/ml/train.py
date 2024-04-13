from ..utils.common import get_logger
from ..domain.config import Config
import pandas as pd
from typing import List
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump

logger = get_logger()


def train(df: pd.DataFrame, feature_columns: List[str], config: Config):
    """
    Train and save model.
    """
    logger.info("Started train")
    reg = _train(df, feature_columns, config)
    _log_traning_mertrics(reg, df, feature_columns, config)
    _store_model(reg, config)
    logger.info("Completed train")
    return df


def _train(
    df: pd.DataFrame, feature_columns: List[str], config: Config
) -> GradientBoostingRegressor:
    X = df[feature_columns].values
    y = df[config.target].values
    reg = GradientBoostingRegressor(**config.model_params)
    reg.fit(X, y)
    return reg


def _log_traning_mertrics(
    reg: GradientBoostingRegressor,
    df: pd.DataFrame,
    feature_columns: List[str],
    config: Config,
):
    X = df[feature_columns].values
    y = df[config.target].values
    y_pred = reg.predict(X)
    mse = np.sqrt(mean_squared_error(y, y_pred))
    logger.info(f"Training metrics: mse={mse}")


def _store_model(reg: GradientBoostingRegressor, config: Config):
    name = "gbr"
    fp = config.models_path / f"{name}_{config.model_id}.pkl"
    dump(reg, fp)
    logger.info(f"Stored encoder: name={name};file={str(fp)}")
