
-- Задание 1: Выбрать всех студентов с возрастом не больше 17 или рейтингом не равным 90
SELECT * FROM Студенты WHERE возраст <= 17 OR рейтинг <> 90;

-- Задание 2: Выбрать студентов, у которых есть запись в отношении «Абонемент» с количеством книг более 5 и задолженностью 1
SELECT Студенты.Номер_зачетной_книжки, Студенты.ФИО, Студенты.Номер_читательского_билета
FROM Студенты
JOIN Абонемент ON Студенты.Номер_зачетной_книжки = Абонемент.Номер_зачетной_книжки
WHERE Абонемент.Количество_книг > 5 AND Абонемент.Задолженность = 1;

-- Задание 3: Выбрать всех менеджеров, имеющих льготы с номером 3
SELECT Сотрудники.*
FROM Сотрудники
JOIN Льготники ON Сотрудники.Табельный_номер = Льготники.Табельный_номер
WHERE Сотрудники.должность = 'менеджер' AND Льготники.Номер_льготы = 3;

-- Задание 4: Создать список сотрудников, которые больше не пойдут в отпуск в текущем году
SELECT Сотрудник.*
FROM Сотрудник
WHERE NOT EXISTS (
    SELECT 1 FROM Отпуска
    WHERE Сотрудник.Табельный_номер = Отпуска.Табельный_номер AND Отпуска.Год = YEAR(CURDATE())
);
