# COMP3303A-A3-Q1
Repo for COMP3303A Assignment 3 Question 1

## Setup
1. On terminal at project root:
- python -m venv venv
- venv/scripts/activate (windows)
- pip install psycopg2
- pip freeze > requirements.txt
2. Make your IDE use the virtual environment you just created.
3. Setup postgres database with initial data
4. Create database.ini with (and modify with your real values):
```
[postgresql]
host=localhost
database=databaseName
user=YourUsername
password=YourPassword
```
5. Run connect.py to test your credentials (Should show: Connected to PostgreSQL server.).
6. Run main.py to test functionality.

## Initial data
CREATE TABLE students(
	student_id serial PRIMARY KEY,
	first_name varchar(25) NOT NULL,
	last_name varchar(25) NOT NULL,
	email varchar(25) NOT NULL UNIQUE,
	enrollment_date date
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

## Video: