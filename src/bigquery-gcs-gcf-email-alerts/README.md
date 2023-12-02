# bigquery-gcs-gcf-email-alerts

![](/src/bigquery-gcs-gcf-email-alerts/img/Email%20Alerts%20for%20BigQuery%20Data.png)

- Create new GCP project
- Save and schedule new SQL query (`src/query.sql`)
- Create new cloud storage bucket:
```
>>> gcloud config set project smoothie-bowl-king
>>> PROJECT_ID=$(gcloud config get project)
>>> BUCKET_ID=${PROJECT_ID}-email-csvs
>>> gcloud storage buckets create gs://${BUCKET_ID} --location us-central1
```
- Create new cloud storage function (`src/index.js` & `src/package.json`)
- Create sendgrid account and get API credentials
- Test from BigQuery
- Test from CLI:
```
>>> cat > HELLO_FRIEND.txt
Hello from the command line!
>>> gcloud storage cp HELLO_FRIEND.txt gs://${BUCKET_ID}
```
