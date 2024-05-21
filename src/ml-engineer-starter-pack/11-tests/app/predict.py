import argparse
from pathlib import Path

import numpy as np

from ml_app.dataprep.prep_filter import prep_filter
from ml_app.dataprep.prep_load import prep_load
from ml_app.feateng.feat_bin import feat_bin
from ml_app.ml.predict import predict

parser = argparse.ArgumentParser()
parser.add_argument("--predict-data", "-f", help="Training data CSV", required=True)
parser.add_argument("--model-id", "-i", help="Unique model ID", required=True)
args = parser.parse_args()

SEED = 18

print(f"Starting predict: model_id={args.model_id}")
np.random.seed(SEED)
df = prep_load(Path(args.predict_data))
df = prep_filter(df, for_pred=True)
df = feat_bin(df)
predict(df, args.model_id)
print(f"Completed predict: model_id={args.model_id}")
