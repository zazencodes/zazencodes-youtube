from ..utils.common import get_logger
import pandas as pd

logger = get_logger()


def feat_ts(df: pd.DataFrame):
    """
    Feature engineer timeseries variables.
    """
    logger.info("Started feateng: step=ts")
    df = _add_ts_features(df)
    logger.info("Completed feateng: step=ts")
    return df


def _add_ts_features(df: pd.DataFrame) -> pd.DataFrame:
    g = ["center_id", "meal_id"]

    # Num orders from past week
    df["num_orders_shift_1"] = df.groupby(g).num_orders.shift(1)

    # Num orders same week last year
    df["num_orders_shift_52"] = df.groupby(g).num_orders.shift(52)

    # Num orders rolling average past 4 weeks
    df["num_orders_rolling_4"] = (
        df.groupby(g).num_orders.rolling(4).mean().reset_index(drop=True)
    )

    # Num orders rolling average past 16 weeks
    df["num_orders_rolling_16"] = (
        df.groupby(g).num_orders.rolling(16).mean().reset_index(drop=True)
    )

    # Num order rolling averages from same week last year
    df["num_orders_rolling_4_shift_52"] = df.groupby(g).num_orders_rolling_4.shift(52)
    df["num_orders_rolling_16_shift_52"] = df.groupby(g).num_orders_rolling_16.shift(52)

    return df
