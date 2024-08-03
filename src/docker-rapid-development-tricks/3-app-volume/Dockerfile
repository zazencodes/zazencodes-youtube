FROM python:3.12-slim
RUN pip install pandas==2.2.2 scikit-learn==1.5.1
ENV PYTHONUNBUFFERED=1
COPY app app
CMD ["python", "-m", "http.server"]
