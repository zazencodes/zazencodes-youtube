FROM python:3.12-slim

WORKDIR /app

RUN pip install scikit-learn==1.5.1 flask==3.0.3 psycopg2-binary==2.9.9 redis==5.0.7

EXPOSE 5001

CMD ["python", "prediction_server.py"]
