import argparse
from pathlib import Path

import numpy as np

from ml_app.dataprep.prep_filter import prep_filter
from ml_app.dataprep.prep_load import prep_load
from ml_app.feateng.feat_bin import feat_bin
from ml_app.ml.train import train

parser = argparse.ArgumentParser()
parser.add_argument("--train-data", "-f", help="Training data CSV", required=True)
parser.add_argument("--model-id", "-i", help="Unique model ID", required=True)
args = parser.parse_args()

SEED = 18

print(f"Starting model training: model_id={args.model_id}")
np.random.seed(SEED)
df = prep_load(Path(args.train_data))
df = prep_filter(df)
df = feat_bin(df)
train(df, args.model_id)
print(f"Completed model training: model_id={args.model_id}")
