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
