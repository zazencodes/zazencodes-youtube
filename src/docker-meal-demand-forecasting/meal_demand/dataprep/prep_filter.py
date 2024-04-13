from ..utils.common import get_logger
import pandas as pd


logger = get_logger()


def prep_filter(df: pd.DataFrame):
    """
    Filter data before training, after feature engineering and one-hot encoding.

    Drop NaN rows introduced with feature engineering.
    """
    logger.info("Started dataprep: step=filter")
    df = _drop_nan_rows(df)
    logger.info("Completed dataprep: step=filter")
    return df


def _drop_nan_rows(df: pd.DataFrame) -> pd.DataFrame:
    len_0 = len(df)
    df = df.dropna()
    len_diff = len_0 - len(df)
    logger.info(f"Droped {len_diff} rows ({len_diff/len_0*100:.1f}%)")
    return df
