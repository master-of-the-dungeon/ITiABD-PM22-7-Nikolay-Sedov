
-- Inserting single rows without column names
INSERT INTO courses VALUES (DEFAULT, 'Introduction to SQL', 'Learn the basics of SQL', 'Development', DEFAULT, DEFAULT);
INSERT INTO instructors VALUES (DEFAULT, 'John', 'Doe', 'john.doe@example.com', 'Expert in SQL and databases');
INSERT INTO students VALUES (DEFAULT, 'Jane', 'Smith', 'jane.smith@example.com', DEFAULT);
INSERT INTO enrollments VALUES (DEFAULT, 1, 1, DEFAULT, 0);
INSERT INTO course_materials VALUES (DEFAULT, 1, 'SQL Basics', 'SQL course material', DEFAULT);

-- Inserting single rows with column names in table order
INSERT INTO courses (course_id, title, description, category, created_at, updated_at) 
VALUES (DEFAULT, 'Advanced CSS', 'Styling complex websites', 'Design', DEFAULT, DEFAULT);

-- Inserting single rows with column names in different order
INSERT INTO students (first_name, last_name, email, student_id, registration_date) 
VALUES ('Alice', 'Johnson', 'alice.johnson@example.com', DEFAULT, DEFAULT);

-- Inserting a group of rows without column names
INSERT INTO instructors VALUES 
(DEFAULT, 'Dave', 'Brown', 'dave.brown@example.com', 'Expert in Java'),
(DEFAULT, 'Sam', 'Davis', 'sam.davis@example.com', 'Expert in Python');

-- Inserting a group of rows with column names
INSERT INTO courses (title, description, category) VALUES 
('Graphic Design Basics', 'Learn design principles', 'Design'),
('Marketing Fundamentals', 'Understand the basics of marketing', 'Marketing');

-- Inserting rows with default values
INSERT INTO students (first_name, last_name, email) VALUES 
('Bob', 'White', 'bob.white@example.com');

-- Inserting multiple rows and returning all fields
INSERT INTO enrollments (student_id, course_id, progress) VALUES 
(2, 1, 25),
(3, 2, 50)
RETURNING *;

-- Upsert: Insert a row and replace in case of conflict
INSERT INTO courses (course_id, title, description, category) VALUES 
(1, 'Introduction to SQL', 'Learn SQL basics and queries', 'Development')
ON CONFLICT (course_id) DO UPDATE SET 
title = EXCLUDED.title, 
description = EXCLUDED.description, 
category = EXCLUDED.category;
