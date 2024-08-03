from flask import Flask, request, jsonify

import psycopg2
import redis
from pickle import load
import os

app = Flask(__name__)

# Connect to Postgres
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port="5432",
)
cursor = conn.cursor()

# Connect to Redis
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379)

# Load model
with open("/artifacts/linear_regression_model.pkl", "rb") as f:
    model = load(f)


@app.route("/test")
def test():
    print("/test endpoint is ok")
    return "Success!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    X = [[data["x1"], data["x2"]]]
    prediction = float(model.predict(X)[0])
    r.set("last_prediction", prediction)
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS predictions (id SERIAL PRIMARY KEY, prediction FLOAT);"
    )
    cursor.execute("INSERT INTO predictions (prediction) VALUES (%s);", (prediction,))
    conn.commit()
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
