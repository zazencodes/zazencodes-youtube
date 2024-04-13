from ..utils.common import get_logger
from ..domain.config import Config
import pandas as pd
from typing import Dict, List, Tuple
from sklearn.preprocessing import OneHotEncoder
from joblib import dump

logger = get_logger()


def prep_ohe(df: pd.DataFrame, config: Config) -> Tuple[pd.DataFrame, List[str]]:
    """
    Add one-hot-encoded features for nominal variables and save encoders.
    """
    logger.info("Started dataprep: step=ohe")
    encoders = _fit_ohe(df, config)
    df, ohe_processed_features = _add_ohe_features(df, encoders)
    _store_encoders(encoders, config)
    logger.info("Completed dataprep: step=ohe")
    return df, ohe_processed_features


def _fit_ohe(df: pd.DataFrame, config: Config) -> Dict[str, OneHotEncoder]:
    ohe = OneHotEncoder()
    encoders = {}
    for col in config.ohe_features:
        ohe = OneHotEncoder()
        ohe.fit(df[[col]].values)
        encoders[col] = ohe
    return encoders


def _add_ohe_features(
    df: pd.DataFrame, encoders: Dict[str, OneHotEncoder]
) -> Tuple[pd.DataFrame, List[str]]:
    ohe_dfs = []
    ohe_cols = []
    for col, ohe in encoders.items():
        X_ohe = ohe.transform(df[[col]])
        cols = [f"{col}_ohe_{i}" for i in range(X_ohe.shape[1])]  # pyright: ignore
        ohe_cols += cols
        ohe_dfs.append(
            pd.DataFrame(X_ohe.toarray(), dtype=int, columns=cols)  # pyright: ignore
        )

    df_ohes = pd.concat(ohe_dfs, axis=1)
    df = pd.concat((df, df_ohes), axis=1)
    return df, ohe_cols


def _store_encoders(encoders: Dict[str, OneHotEncoder], config: Config):
    for name, ohe in encoders.items():
        fp = config.models_path / f"ohe_{name}_{config.model_id}.pkl"
        dump(ohe, str(fp))
        logger.info(f"Stored encoder: name={name};file={str(fp)}")
