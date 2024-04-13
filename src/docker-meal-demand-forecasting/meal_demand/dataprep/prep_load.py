from ..utils.common import get_logger
from ..domain.config import Config
from typing import Dict
import pandas as pd

logger = get_logger()


def prep_load(config: Config):
    """
    Load and merge raw dataset.
    """
    logger.info("Started dataprep: step=load")
    logger.info("Started dataprep: step=load")
    dfs = _load(config)
    df = _merge(dfs)
    df = _center_type_filter(df, config.center_type)
    logger.info("Completed dataprep: step=load")
    return df


def _load(config: Config) -> Dict[str, pd.DataFrame]:
    df_center_info = pd.read_csv(config.data_path / config.fulfilment_center_file)
    df_meal_info = pd.read_csv(config.data_path / config.meal_info_file)
    df_train_raw = pd.read_csv(config.data_path / config.train_file)

    dfs = dict(
        center_info=df_center_info,
        meal_info=df_meal_info,
        train_raw=df_train_raw,
    )
    for name, df in dfs.items():
        logger.info(f"Loaded data: name={name};len={len(df)}")

    return dfs


def _merge(dfs: Dict[str, pd.DataFrame]):
    df = dfs["train_raw"]
    len_0 = len(df)

    df = pd.merge(df, dfs["center_info"], on="center_id")
    df = pd.merge(df, dfs["meal_info"], on="meal_id")

    if len(df) != len_0:
        raise ValueError(
            "Change in row count after merge. "
            "Check dimension tables for duplication on merge keys."
        )
    return df


def _center_type_filter(df: pd.DataFrame, center_type: str | None) -> pd.DataFrame:
    if not center_type:
        return df

    df = df[df.center_type == center_type]  # pyright: ignore
    return df
