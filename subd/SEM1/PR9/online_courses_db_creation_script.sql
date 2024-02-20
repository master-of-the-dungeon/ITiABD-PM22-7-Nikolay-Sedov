
-- Создание таблицы Курсы
CREATE TABLE Courses (
    CourseID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Difficulty VARCHAR(50) NOT NULL CHECK (Difficulty IN ('Beginner', 'Intermediate', 'Advanced'))
);

-- Создание таблицы Инструкторы
CREATE TABLE Instructors (
    InstructorID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Specialization VARCHAR(255) NOT NULL
);

-- Создание таблицы Студенты
CREATE TABLE Students (
    StudentID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Создание таблицы Записи на курсы
CREATE TABLE Enrollments (
    EnrollmentID SERIAL PRIMARY KEY,
    StudentID INT REFERENCES Students(StudentID) ON DELETE CASCADE,
    CourseID INT REFERENCES Courses(CourseID) ON DELETE SET NULL,
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE,
    Progress INT CHECK (Progress BETWEEN 0 AND 100)
);

-- Создание таблицы Тесты
CREATE TABLE Tests (
    TestID SERIAL PRIMARY KEY,
    CourseID INT REFERENCES Courses(CourseID) ON DELETE CASCADE,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    MaxScore INT CHECK (MaxScore > 0)
);
