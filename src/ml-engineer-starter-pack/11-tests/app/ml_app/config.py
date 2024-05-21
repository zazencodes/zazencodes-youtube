from pathlib import Path

MODEL_PATH = Path("models")
RESULT_PATH = Path("predictions")

TARGET_COLUMN = "Global_Sales"
FEATURE_COLUMNS = ["Critic_Score", "Platform", "Genre", "Publisher"]
CATEGORICAL_FEATURES = [False, True, True, True]
ID_COLUMNS = ["Name"]

MIN_CRITIC_COUNT = 3
MIN_BIN_SIZE = 20

MODEL_PARAMS = dict(
    loss="squared_error",
    learning_rate=0.1,
    max_iter=100,
    max_leaf_nodes=31,
    min_samples_leaf=20,
    categorical_features=CATEGORICAL_FEATURES,
)
