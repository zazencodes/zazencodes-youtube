import pandas as pd

from ..config import (FEATURE_COLUMNS, ID_COLUMNS, MIN_CRITIC_COUNT,
                      TARGET_COLUMN)
from ..utils.common import get_logger

logger = get_logger()


def prep_filter(df: pd.DataFrame, for_pred=False):
    """
    Load and merge raw dataset.
    """
    logger.info("Started dataprep: step=filter")

    # Filter on minimum Critic_Count
    df = df[df.Critic_Count.fillna(0).astype(float) >= MIN_CRITIC_COUNT]

    # Filter on required fields
    cols = []
    cols += FEATURE_COLUMNS
    cols += ID_COLUMNS
    if not for_pred:
        cols.append(TARGET_COLUMN)
    df = df[cols]

    logger.info(f"Filtered data: rows={len(df)};columns={df.columns.tolist()}")
    logger.info("Completed dataprep: step=filter")
    return df
