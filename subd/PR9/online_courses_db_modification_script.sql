
-- a.1. Добавление столбца 'Duration' в таблицу 'Courses'
ALTER TABLE Courses ADD COLUMN Duration INT;

-- a.2. Удаление столбца 'Difficulty' из таблицы 'Courses'
ALTER TABLE Courses DROP COLUMN Difficulty;

-- a.3. Изменение ограничения 'CHECK' для столбца 'Progress' в таблице 'Enrollments'
ALTER TABLE Enrollments DROP CONSTRAINT check_progress;
ALTER TABLE Enrollments ADD CONSTRAINT check_progress CHECK (Progress IN (0, 100));

-- б. Создание дополнительной таблицы 'CourseMaterials'
CREATE TABLE CourseMaterials (
    MaterialID SERIAL PRIMARY KEY,
    CourseID INT,
    Content TEXT
);

-- в. Добавление столбца 'FileType' в таблицу 'CourseMaterials'
ALTER TABLE CourseMaterials ADD COLUMN FileType VARCHAR(50);

-- г. Создание ограничения внешнего ключа для связи 'CourseMaterials' с 'Courses'
ALTER TABLE CourseMaterials ADD CONSTRAINT fk_course FOREIGN KEY (CourseID) REFERENCES Courses (CourseID);

-- д. Изменение типа столбца 'Email' в таблице 'Students'
ALTER TABLE Students ALTER COLUMN Email TYPE TEXT;

-- е. Удаление столбца 'Specialization' из таблицы 'Instructors'
ALTER TABLE Instructors DROP COLUMN Specialization;

-- ж. Удаление таблицы 'Tests'
DROP TABLE Tests;
