
-- Запросы с математическими функциями
SELECT SQRT(COUNT(*)) FROM Записи_на_курсы GROUP BY Курс_ID;
SELECT ROUND(YEAR(CURDATE()) - YEAR(Дата_рождения)) FROM Студенты;
SELECT ABS(YEAR(Дата_окончания) - YEAR(Дата_начала)) FROM Курсы;
SELECT MAX(YEAR(CURDATE()) - YEAR(Дата_рождения)), MIN(YEAR(CURDATE()) - YEAR(Дата_рождения)) FROM Студенты;

-- Запросы с случайной и тригонометрической функциями
SELECT * FROM Студенты ORDER BY RAND() LIMIT 1;
SELECT SIN(ID) FROM Курсы;

-- Запросы для работы со строками
SELECT ФИО || ' ' || Электронная_почта FROM Студенты;
SELECT POSITION('Python' IN Описание) FROM Курсы WHERE Описание LIKE '%Python%';
SELECT SUBSTRING(Название FROM 1 FOR 5) FROM Курсы;
SELECT TRIM(BOTH 'a' FROM Электронная_почта) FROM Студенты;
SELECT INITCAP(Название) FROM Курсы;
SELECT LEFT(ФИО, 5) FROM Студенты;
SELECT CONCAT_WS('-', ФИО, Электронная_почта) FROM Студенты;
SELECT PG_CLIENT_ENCODING();
SELECT MD5(ФИО) FROM Студенты;

-- Запросы с использованием CASE
SELECT ID, Название, CASE WHEN DATEDIFF(Дата_окончания, Дата_начала) > 90 THEN 'Долгий' ELSE 'Короткий' END AS Длительность FROM Курсы;
SELECT ФИО, CASE WHEN YEAR(CURDATE()) - YEAR(Дата_рождения) < 25 THEN 'Молодой' WHEN YEAR(CURDATE()) - YEAR(Дата_рождения) < 35 THEN 'Взрослый' ELSE 'Старший' END AS Возрастная_группа FROM Студенты;

-- Запросы с использованием COALESCE и NULLIF
SELECT COALESCE(Дата_окончания, 'Неизвестно') FROM Курсы;
SELECT NULLIF(Электронная_почта, 'example@example.com') FROM Студенты;
