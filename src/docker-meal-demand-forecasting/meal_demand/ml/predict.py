from ..utils.common import get_logger
from ..domain.config import Config
import pandas as pd
from typing import List
from sklearn.ensemble import GradientBoostingRegressor
from joblib import load

logger = get_logger()


def predict(
    df: pd.DataFrame,
    feature_columns: List[str],
    config: Config,
    center_id: str,
    meal_id: str,
):
    """
    Preict next week demand
    """
    logger.info(f"Started predict: center_type={config.center_type};")
    y_pred = _predict(df, feature_columns, config, center_id, meal_id)
    logger.info(f"Predicted number of orders: {y_pred}")
    logger.info(f"Completed predict center_type={config.center_type};")
    return df


def _predict(
    df: pd.DataFrame,
    feature_columns: List[str],
    config: Config,
    center_id: str,
    meal_id: str,
) -> List[float]:

    idx = (
        (df.center_id == int(center_id))
        & (df.meal_id == int(meal_id))
        & (df.week == config.max_week)
    )
    logger.info(idx)

    X = df[feature_columns][idx].values
    logger.info(f"Making prediction for: {X}")
    reg = _load_model(config)
    y_pred = reg.predict(X)
    return y_pred


def _load_model(config: Config) -> GradientBoostingRegressor:
    name = "gbr"
    center_type_name_prefix = f"_{config.center_type}" if config.center_type else ""
    fp = config.models_path / f"{name}{center_type_name_prefix}_{config.model_id}.pkl"
    reg = load(fp)
    logger.info(
        f"Model loaded: name={name};center_type={config.center_type};file={str(fp)}"
    )
    return reg
