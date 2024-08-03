import psycopg2

# Connect to Postgres
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='mysecretpassword',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, data VARCHAR(100));")
conn.commit()

# Insert data
cursor.execute("INSERT INTO test (data) VALUES ('hello world');")
conn.commit()

# Query data
cursor.execute("SELECT * FROM test;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
