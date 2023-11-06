
-- Скрипт для создания базы данных и ее таблиц, заполнения таблиц данными

-- Создание таблиц (переиспользуем скрипт создания таблиц, который мы уже сформировали)

-- Создание таблицы Курсы
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_category CHECK (category IN ('Development', 'Business', 'IT & Software', 'Design', 'Marketing'))
);

-- Создание таблицы Инструкторы
CREATE TABLE instructors (
    instructor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    biography TEXT,
    CONSTRAINT chk_email_format CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$')
);

-- Создание таблицы Студенты
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT chk_email_format CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$')
);

-- Создание таблицы Записи на курсы
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
    course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE RESTRICT,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    progress INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_progress CHECK (progress BETWEEN 0 AND 100)
);

-- Создание таблицы Материалы курса
CREATE TABLE course_materials (
    material_id SERIAL PRIMARY KEY,
    course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    content_type VARCHAR(50) NOT NULL DEFAULT 'text',
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Создание таблицы Тесты
CREATE TABLE tests (
    test_id SERIAL PRIMARY KEY,
    course_id INT NOT NULL REFERENCES courses(course_id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    max_score INT CHECK (max_score > 0),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- Вставка данных в таблицы (переиспользуем скрипт вставки данных, который мы уже сформировали)

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


-- Создание копии исходной базы данных с новым именем
-- Внимание: Команда должна быть выполнена в командной строке psql, а не в SQL-скрипте
-- CREATE DATABASE new_database_name TEMPLATE original_database_name;

-- Обновление значений некоторых полей таблиц
UPDATE courses SET title = 'Updated Title' WHERE course_id = 1;

-- Удаление строк из таблицы
DELETE FROM students WHERE student_id IN (SELECT student_id FROM enrollments WHERE progress < 50);

-- Добавление новой таблицы
CREATE TABLE additional_table (
    id SERIAL PRIMARY KEY,
    dummy_column VARCHAR(255) DEFAULT 'default_value'
);

-- Заполнение новой таблицы значениями по умолчанию
INSERT INTO additional_table (dummy_column) SELECT DEFAULT FROM generate_series(1, 25);

-- Обновление всех строк новой таблицы
UPDATE additional_table SET dummy_column = 'updated_value';

-- Удаление всех строк новой таблицы
DELETE FROM additional_table;

-- Кодировка (если необходимо, например, для UTF-8)
-- SET client_encoding = 'UTF8';
