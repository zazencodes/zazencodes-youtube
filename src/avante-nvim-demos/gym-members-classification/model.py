import logging

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def create_random_forest_model() -> RandomForestClassifier:
    logging.info("Loading dataset...")
    # Load the dataset
    data = pd.read_csv("../data/gym_members_exercise_tracking.csv")

    # One-hot encode the "Gender" column
    data = pd.get_dummies(data, columns=["Gender"], drop_first=True)

    y = data["Workout_Type"]  # Target variable
    X = data.drop(columns=["Workout_Type"])  # Features

    # Create and fit the model
    model = RandomForestClassifier()
    logging.info("Fitting the Random Forest model...")
    model.fit(X, y)

    return model


def save_model_to_disk(model: RandomForestClassifier) -> None:
    logging.info("Saving model to disk...")
    joblib.dump(model, "../models/gym_forest.pkl")


def load_model_from_disk() -> RandomForestClassifier:
    logging.info("Loading model from disk...")
    return joblib.load("../models/gym_forest.pkl")


def make_predictions(model: RandomForestClassifier) -> None:
    # Load the dataset
    features = pd.read_csv("../data/gym_member_features_to_predict.csv")

    # One-hot encode the "Gender" column
    features = pd.get_dummies(features, columns=["Gender"], drop_first=True)

    # Make predictions
    predictions = model.predict(features)

    # Print features and predictions
    logging.info("Making predictions...")
    for index, row in features.iterrows():
        logging.info("Features: %s | Prediction: %s", row.to_dict(), predictions[index])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the model training and prediction process...")
    model = create_random_forest_model()
    save_model_to_disk(model)

    model = load_model_from_disk()
    make_predictions(model)
