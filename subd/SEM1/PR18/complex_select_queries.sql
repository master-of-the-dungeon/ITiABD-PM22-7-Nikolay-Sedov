-- Запросы с полными именами столбцов и таблиц
SELECT Курсы.ID, Курсы.Название, Курсы.Описание, Курсы.Дата_начала, Курсы.Дата_окончания FROM Курсы;
SELECT Студенты.ID, Студенты.ФИО, Студенты.Дата_рождения, Студенты.Электронная_почта FROM Студенты;

-- Запросы с арифметическими операторами
SELECT ID, Название, (Дата_окончания - Дата_начала) AS Длительность FROM Курсы;
SELECT ФИО, EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM Дата_рождения) AS Возраст FROM Студенты;
SELECT Курс_ID, COUNT(*) AS Количество_студентов FROM Записи_на_курсы GROUP BY Курс_ID;

-- Запросы с логическими операторами
SELECT * FROM Курсы WHERE EXTRACT(YEAR FROM Дата_начала) = 2023 AND EXTRACT(MONTH FROM Дата_окончания) > 3;
SELECT * FROM Студенты WHERE EXTRACT(YEAR FROM Дата_рождения) > 1995 AND EXTRACT(YEAR FROM Дата_рождения) <> 1997;
SELECT * FROM Лекторы WHERE Специализация = 'Программирование' OR Специализация = 'Веб-разработка';

-- Запрос со скалярным подзапросом
SELECT * FROM Курсы WHERE (SELECT COUNT(*) FROM Записи_на_курсы WHERE Курсы.ID = Записи_на_курсы.Курс_ID) > 3;

-- Запросы с разными приведениями типов
SELECT Дата_начала::CHAR FROM Курсы;
SELECT ID::CHAR FROM Курсы;
SELECT Дата_рождения::DATE FROM Студенты;
SELECT Название::TEXT FROM Курсы;
SELECT Электронная_почта::VARCHAR(100) FROM Студенты;

-- Запросы на проверку эквивалентности выражений с учетом NULL
SELECT * FROM Курсы WHERE Дата_окончания IS NULL;
SELECT * FROM Студенты WHERE Электронная_почта IS NOT NULL;
