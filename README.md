# COMP3303A-A3-Q1
Repo for COMP3303A Assignment 3 Question 1

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