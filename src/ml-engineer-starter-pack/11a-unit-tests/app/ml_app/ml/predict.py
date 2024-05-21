from pathlib import Path
from typing import List

import pandas as pd
from joblib import load
from sklearn.ensemble import HistGradientBoostingRegressor

from ..config import TARGET_COLUMN, FEATURE_COLUMNS, ID_COLUMNS, MODEL_PATH, RESULT_PATH
from ..utils.common import get_logger

logger = get_logger()


def predict(
    df: pd.DataFrame,
    model_id: str,
):
    """
    Load model and make prediction.
    """
    logger.info(f"Started predict: model_id={model_id};")
    reg = _load_model(MODEL_PATH, model_id)
    y_pred = _predict(reg, df, FEATURE_COLUMNS)
    logger.info(f"Predicted Global_Sales: {y_pred}")
    _store_predict(RESULT_PATH, df, y_pred, model_id)
    logger.info(f"Completed predict: model_id={model_id};")
    return df


def _predict(
    reg: HistGradientBoostingRegressor,
    df: pd.DataFrame,
    feature_columns: List[str],
) -> List[float]:

    X = df[feature_columns].values
    logger.info(f"Making prediction: num_records={len(df)}")
    y_pred = reg.predict(X)
    return list(y_pred)


def _load_model(model_path: Path, model_id: str) -> HistGradientBoostingRegressor:
    name = "gbr"
    fp = model_path / f"{name}_{model_id}.pkl"
    reg = load(fp)
    logger.info(f"Model loaded: file={str(fp)}")
    return reg


def _store_predict(
    result_path: Path,
    df: pd.DataFrame,
    y_pred: List[float],
    model_id: str,
):
    name = "gbr"

    fp = result_path / f"{name}_{model_id}.csv"
    df_pred = df.copy()
    df_pred[f"Pred_{TARGET_COLUMN}"] = y_pred
    df_pred.to_csv(str(fp), index=False)
    logger.info(f"Stored table: file={str(fp)}")

    fp = result_path / f"{name}_{model_id}.json"
    fp.write_text(
        df_pred[ID_COLUMNS + [f"Pred_{TARGET_COLUMN}"]].to_json(
            orient="records", indent=2
        )
    )
    logger.info(f"Stored result: file={str(fp)}")
