# SQL

Start database

```bash
docker run --name zc_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
docker ps
docker exec -it zc_postgres /bin/bash
psql -U postgres

# List current database
\c
```

Create sample tables

```sql
-- Create the employees table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    department VARCHAR(128)
);

-- Create the salaries table
CREATE TABLE salaries (
    salary_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(employee_id),
    base_salary FLOAT,
    bonus FLOAT
);

-- Insert sample data into employees table
INSERT INTO employees (first_name, last_name, department) VALUES
('John', 'Doe', 'Engineering'),
('Jane', 'Smith', 'Marketing'),
('Sam', 'Brown', 'HR');

-- Insert sample data into salaries table
INSERT INTO salaries (employee_id, base_salary, bonus) VALUES
(1, 60000, 5000),
(2, 55000, 7000),
(3, 50000, 3000);
```

Query data

```sql
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT AVG(base_salary) FROM salaries;
SELECT employee_id, base_salary + bonus AS total_salary FROM salaries;
SELECT CONCAT(e.first_name, ' ', e.last_name) AS name, s.base_salary + s.bonus AS total_salary FROM salaries s JOIN employees e ON s.employee_id = e.employee_id;
```



