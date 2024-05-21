import pandas as pd

from ..config import CATEGORICAL_FEATURES, FEATURE_COLUMNS, MIN_BIN_SIZE
from ..utils.common import get_logger

logger = get_logger()


def feat_bin(df: pd.DataFrame):
    """
    Bin categorical features into "Other" if less than MIN_BIN_SIZE
    """
    logger.info("Started feateng: step=bin")

    for col, is_cat in zip(FEATURE_COLUMNS, CATEGORICAL_FEATURES):
        if not is_cat:
            continue
        bin_counts = df[col].value_counts()
        bin_labels = bin_counts.where(bin_counts < MIN_BIN_SIZE).dropna().index.tolist()
        m = df[col].isin(bin_labels)
        logger.info(f"Setting {m.sum()} rows to 'Other' for {col}")
        df.loc[m, col] = "Other"

    logger.info("Completed feateng: step=bin")
    return df
