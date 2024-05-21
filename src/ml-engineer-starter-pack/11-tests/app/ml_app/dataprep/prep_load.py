from pathlib import Path

import pandas as pd

from ..utils.common import get_logger

logger = get_logger()

MIN_CRITIC_COUNT = 3


def prep_load(input_data: Path):
    """
    Load and merge raw dataset.
    """
    logger.info("Started dataprep: step=load")

    # Load from CSV
    df = pd.read_csv(input_data)

    logger.info(
        f"Loaded data: file={input_data};rows={len(df)};columns={df.columns.tolist()}"
    )
    logger.info("Completed dataprep: step=load")
    return df
