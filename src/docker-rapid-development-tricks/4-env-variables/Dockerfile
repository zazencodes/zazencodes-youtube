FROM python:3.12-slim

WORKDIR /app

RUN pip install scikit-learn==1.5.1

COPY train_model.py .

CMD ["python", "train_model.py"]

