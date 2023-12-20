-- Создание таблиц
CREATE TABLE Студенты (
    Номер_зачетной_книжки INT PRIMARY KEY,
    ФИО VARCHAR(100),
    Возраст INT,
    Рейтинг INT,
    Номер_читательского_билета INT
);

CREATE TABLE Абонемент (
    Номер_зачетной_книжки INT,
    Количество_книг INT,
    Задолженность INT,
    FOREIGN KEY (Номер_зачетной_книжки) REFERENCES Студенты(Номер_зачетной_книжки)
);

CREATE TABLE Сотрудники (
    Табельный_номер INT PRIMARY KEY,
    ФИО VARCHAR(100),
    Должность VARCHAR(50)
);

CREATE TABLE Льготники (
    Табельный_номер INT,
    Номер_льготы INT,
    FOREIGN KEY (Табельный_номер) REFERENCES Сотрудники(Табельный_номер)
);

CREATE TABLE Отпуска (
    Табельный_номер INT,
    Год INT,
    FOREIGN KEY (Табельный_номер) REFERENCES Сотрудники(Табельный_номер)
);

-- Заполнение таблиц тестовыми данными
-- Студенты
INSERT INTO Студенты VALUES (1, 'Иван Иванов', 16, 88, 101);
INSERT INTO Студенты VALUES (2, 'Петр Петров', 18, 90, 102);
INSERT INTO Студенты VALUES (3, 'Сидор Сидоров', 17, 91, 103);
INSERT INTO Студенты VALUES (4, 'Анна Аннова', 19, 89, 104);

-- Абонемент
INSERT INTO Абонемент VALUES (1, 6, 1);
INSERT INTO Абонемент VALUES (3, 4, 0);
INSERT INTO Абонемент VALUES (4, 7, 1);

-- Сотрудники
INSERT INTO Сотрудники VALUES (1, 'Алексей Алексеев', 'менеджер');
INSERT INTO Сотрудники VALUES (2, 'Ольга Ольгина', 'бухгалтер');
INSERT INTO Сотрудники VALUES (3, 'Ирина Ирина', 'менеджер');

-- Льготники
INSERT INTO Льготники VALUES (1, 3);
INSERT INTO Льготники VALUES (3, 2);

-- Отпуска
INSERT INTO Отпуска VALUES (1, 2023);
INSERT INTO Отпуска VALUES (2, 2022);
