EXPORT DATA OPTIONS(
  uri='gs://smoothie-bowl-king-email-csvs/emerging_trends_*.csv',
  format='CSV',
  overwrite=true,
  header=true,
  field_delimiter=','
) AS (
WITH
  max_week AS (
  SELECT
    MAX(week) AS value
  FROM
    `bigquery-public-data.google_trends.top_rising_terms`
  WHERE
    refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY) )
SELECT
  term,
  rank,
  percent_gain
FROM
  `bigquery-public-data.google_trends.top_rising_terms`,
  max_week
WHERE
  refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND week = max_week.value
GROUP BY
  term,
  rank,
  percent_gain
ORDER BY
  rank ASC
LIMIT
  100
);
