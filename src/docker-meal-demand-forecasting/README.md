# Meal Demand

## Train Model

Model binaries are daved to `data/models` folder.

```bash
docker build -t meal-demand .
docker run \
    -v ./data:/data \
    -v ./models:/models \
    -v ./meal_demand:/app/meal_demand \
    meal-demand train_model.py
```

Train model for center type, e.g. TYPE_A


```bash
docker run \
    -v ./data:/data \
    -v ./models:/models \
    -v ./meal_demand:/app/meal_demand \
    -e CENTER_TYPE=TYPE_A \
    meal-demand train_model.py
```

Make a prediction

```bash
docker run \
    -v ./data:/data \
    -v ./models:/models \
    -v ./meal_demand:/app/meal_demand \
    -e MODEL_ID=fb4d6 \
    [-e CENTER_TYPE=TYPE_A \]
    meal-demand predict.py --center-id=177 --meal-id=1445
```
