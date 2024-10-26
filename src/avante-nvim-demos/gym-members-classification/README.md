# Gym Members Classification

This project aims to classify gym members based on their exercise tracking data using a Random Forest model.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gym-members-classification
   ```

2. Install the required packages in a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your dataset in the `data` directory.
2. Run the model training and prediction script:
   ```bash
   python model.py
   ```

## Model

The model is built using the `RandomForestClassifier` from `sklearn`. It predicts the workout type based on the features provided in the dataset.

## License

This project is licensed under the MIT License.
