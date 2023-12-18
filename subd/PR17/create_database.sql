
-- Создание таблицы Курсы
CREATE TABLE Курсы (
    ID INT PRIMARY KEY,
    Название VARCHAR(100),
    Описание TEXT,
    Дата_начала DATE,
    Дата_окончания DATE
);

-- Создание таблицы Лекторы
CREATE TABLE Лекторы (
    ID INT PRIMARY KEY,
    ФИО VARCHAR(100),
    Специализация VARCHAR(100),
    Контактные_данные VARCHAR(100)
);

-- Создание таблицы Студенты
CREATE TABLE Студенты (
    ID INT PRIMARY KEY,
    ФИО VARCHAR(100),
    Дата_рождения DATE,
    Электронная_почта VARCHAR(100)
);

-- Создание таблицы Записи на курсы
CREATE TABLE Записи_на_курсы (
    ID INT PRIMARY KEY,
    Курс_ID INT,
    Студент_ID INT,
    FOREIGN KEY (Курс_ID) REFERENCES Курсы(ID),
    FOREIGN KEY (Студент_ID) REFERENCES Студенты(ID)
);

-- Создание таблицы Материалы курсов
CREATE TABLE Материалы_курсов (
    ID INT PRIMARY KEY,
    Курс_ID INT,
    Название VARCHAR(100),
    Тип VARCHAR(50),
    Ссылка VARCHAR(100),
    FOREIGN KEY (Курс_ID) REFERENCES Курсы(ID)
);
