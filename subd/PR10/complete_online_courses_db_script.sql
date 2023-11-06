
-- Создание таблицы Курсы
CREATE TABLE IF NOT EXISTS Courses (
    CourseID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Difficulty VARCHAR(50) NOT NULL CHECK (Difficulty IN ('Beginner', 'Intermediate', 'Advanced'))
);

-- Создание таблицы Инструкторы
CREATE TABLE IF NOT EXISTS Instructors (
    InstructorID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Specialization VARCHAR(255) NOT NULL
);

-- Создание таблицы Студенты
CREATE TABLE IF NOT EXISTS Students (
    StudentID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Создание таблицы Записи на курсы
CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID SERIAL PRIMARY KEY,
    StudentID INT REFERENCES Students(StudentID) ON DELETE CASCADE,
    CourseID INT REFERENCES Courses(CourseID) ON DELETE SET NULL,
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE,
    Progress INT CHECK (Progress BETWEEN 0 AND 100)
);

-- Создание таблицы Тесты
CREATE TABLE IF NOT EXISTS Tests (
    TestID SERIAL PRIMARY KEY,
    CourseID INT REFERENCES Courses(CourseID) ON DELETE CASCADE,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    MaxScore INT CHECK (MaxScore > 0)
);

-- Модификации таблиц
-- Добавление столбца 'Duration' в таблицу 'Courses'
ALTER TABLE Courses ADD COLUMN IF NOT EXISTS Duration INT;

-- Удаление столбца 'Difficulty' из таблицы 'Courses'
ALTER TABLE Courses DROP COLUMN IF EXISTS Difficulty;

-- Изменение ограничения 'CHECK' для столбца 'Progress' в таблице 'Enrollments'
ALTER TABLE Enrollments DROP CONSTRAINT IF EXISTS check_progress;
ALTER TABLE Enrollments ADD CONSTRAINT check_progress CHECK (Progress IN (0, 100));

-- Создание дополнительной таблицы 'CourseMaterials'
CREATE TABLE IF NOT EXISTS CourseMaterials (
    MaterialID SERIAL PRIMARY KEY,
    CourseID INT,
    Content TEXT
);

-- Добавление столбца 'FileType' в таблицу 'CourseMaterials'
ALTER TABLE CourseMaterials ADD COLUMN IF NOT EXISTS FileType VARCHAR(50);

-- Создание ограничения внешнего ключа для связи 'CourseMaterials' с 'Courses'
ALTER TABLE CourseMaterials ADD CONSTRAINT IF NOT EXISTS fk_course FOREIGN KEY (CourseID) REFERENCES Courses (CourseID);

-- Изменение типа столбца 'Email' в таблице 'Students'
ALTER TABLE Students ALTER COLUMN Email TYPE TEXT;

-- Удаление столбца 'Specialization' из таблицы 'Instructors'
ALTER TABLE Instructors DROP COLUMN IF EXISTS Specialization;

-- Удаление таблицы 'Tests'
DROP TABLE IF EXISTS Tests;
