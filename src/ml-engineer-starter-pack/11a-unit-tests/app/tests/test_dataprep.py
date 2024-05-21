# import sys
#
# sys.path.append("../")
from pathlib import Path

import pandas as pd
import pytest

from ml_app.config import FEATURE_COLUMNS, ID_COLUMNS, TARGET_COLUMN
from ml_app.dataprep.prep_filter import prep_filter
from ml_app.dataprep.prep_load import prep_load

TRAIN_DATA_FILE = "../../data/train.Video_Games_Sales_as_at_22_Dec_2016.csv"
TRAIN_DATA_LENGTH = 16709


def test_prep_load():
    df = prep_load(Path(TRAIN_DATA_FILE))

    # Correct length
    assert len(df) == TRAIN_DATA_LENGTH


def test_prep_filter():
    df = pd.read_csv(Path(TRAIN_DATA_FILE))
    df = prep_filter(df)

    # Has expected columns
    assert TARGET_COLUMN in df.columns
    assert [col in df.columns for col in FEATURE_COLUMNS]
    assert [col in df.columns for col in ID_COLUMNS]
