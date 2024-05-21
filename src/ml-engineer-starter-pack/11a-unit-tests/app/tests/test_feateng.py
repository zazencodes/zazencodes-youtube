# import sys
#
# sys.path.append("../")
from pathlib import Path

import pandas as pd
import pytest

from ml_app.config import CATEGORICAL_FEATURES, FEATURE_COLUMNS, MIN_BIN_SIZE
from ml_app.dataprep.prep_filter import prep_filter
from ml_app.dataprep.prep_load import prep_load
from ml_app.feateng.feat_bin import feat_bin

TRAIN_DATA_FILE = "../../data/train.Video_Games_Sales_as_at_22_Dec_2016.csv"


def test_feat_bin():
    df = pd.read_csv(Path(TRAIN_DATA_FILE))

    df = feat_bin(df)
    for col, is_cat in zip(FEATURE_COLUMNS, CATEGORICAL_FEATURES):
        if not is_cat:
            continue
        bin_counts = df[col].value_counts()
        bin_labels = bin_counts.where(bin_counts < MIN_BIN_SIZE).dropna().index.tolist()

        bin_labels = set(bin_labels)
        bin_labels.add("Other")

        # No bin labels (except "Other")
        assert len(bin_labels) == 1
