# Unit tests

## Dataset

Dataset: https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings

## Install

```bash
python -m venv venv
venv/bin/pip install -r requirements.txt
```

## Train / predict with model

```bash
MODEL_ID=i8du28
python train_model.py -f ../../data/train.Video_Games_Sales_as_at_22_Dec_2016.csv -i $MODEL_ID
python predict.py -f ../../data/pred.Video_Games_Sales_as_at_22_Dec_2016.csv -i $MODEL_ID
```

## Run unit tests with pytest

```bash
venv/bin/python -m pytest -v
```

