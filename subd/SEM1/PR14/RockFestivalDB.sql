
-- Создание таблицы Фестиваль
CREATE TABLE Фестиваль (
    Название VARCHAR(255) PRIMARY KEY,
    Жанр VARCHAR(255),
    Количество_участников INT
);

-- Создание таблицы Менеджер
CREATE TABLE Менеджер (
    ФИО_менеджера VARCHAR(255) PRIMARY KEY,
    Номер_менеджера VARCHAR(20)
);

-- Создание таблицы Сцена
CREATE TABLE Сцена (
    Название_сцены VARCHAR(255) PRIMARY KEY,
    Площадь_сцены DECIMAL,
    ФИО_ответственного_за_сцену VARCHAR(255)
);

-- Создание таблицы Работник сцены
CREATE TABLE Работник_сцены (
    ФИО_работника_сцены VARCHAR(255) PRIMARY KEY,
    Телефон VARCHAR(20),
    Должность VARCHAR(255),
    Оклад DECIMAL
);

-- Создание таблицы Выступление
CREATE TABLE Выступление (
    Название VARCHAR(255),
    Название_сцены VARCHAR(255),
    ФИО_менеджера VARCHAR(255),
    ФИО_работника_сцены VARCHAR(255),
    Дата_время_начала_выступления DATETIME,
    Длительность INT,
    Гонорар DECIMAL,
    PRIMARY KEY (Название, Дата_время_начала_выступления),
    FOREIGN KEY (Название) REFERENCES Фестиваль(Название),
    FOREIGN KEY (Название_сцены) REFERENCES Сцена(Название_сцены),
    FOREIGN KEY (ФИО_менеджера) REFERENCES Менеджер(ФИО_менеджера),
    FOREIGN KEY (ФИО_работника_сцены) REFERENCES Работник_сцены(ФИО_работника_сцены)
);

-- Если необходимо, создание таблицы Гонорар
CREATE TABLE Гонорар (
    Название VARCHAR(255) PRIMARY KEY,
    Гонорар DECIMAL,
    FOREIGN KEY (Название) REFERENCES Фестиваль(Название)
);
