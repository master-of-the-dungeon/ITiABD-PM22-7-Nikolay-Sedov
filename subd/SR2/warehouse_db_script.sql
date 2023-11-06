
-- Создание таблицы Склады
CREATE TABLE IF NOT EXISTS Warehouses (
    warehouse_number SERIAL PRIMARY KEY,
    address TEXT NOT NULL,
    phone TEXT NOT NULL,
    manager_last_name TEXT,
    area FLOAT DEFAULT 15 CHECK (area >= 15)
);

-- Создание таблицы Товары
CREATE TABLE IF NOT EXISTS Products (
    product_code SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL, -- предполагается замена на внешний ключ
    manufacturer_name TEXT NOT NULL, -- предполагается замена на внешний ключ
    wholesale_price MONEY NOT NULL,
    retail_price MONEY CHECK (retail_price <= wholesale_price * 1.2),
    discount INT -- будет рассчитан и добавлен позже
);

-- Создание таблицы Наличие Товаров
CREATE TABLE IF NOT EXISTS ProductAvailability (
    warehouse_number INT NOT NULL,
    product_code INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (warehouse_number, product_code),
    FOREIGN KEY (warehouse_number) REFERENCES Warehouses(warehouse_number),
    FOREIGN KEY (product_code) REFERENCES Products(product_code)
);

-- Заполнение таблицы Склады данными
INSERT INTO Warehouses (warehouse_number, address, phone, manager_last_name, area) VALUES
(1, 'Первомайская, 1', '111111', 'Иванов', 100),
(2, 'Московское, 7', '222222', 'Сидоров', 150);
-- Добавьте остальные записи по аналогии

-- Заполнение таблицы Товары данными
INSERT INTO Products (name, group_name, manufacturer_name, wholesale_price) VALUES
('Молоток', 'Инструменты', 'Стройгрупп', 100),
('Отвертка', 'Инструменты', 'Стройгрупп', 150);
-- Добавьте остальные записи по аналогии

-- Установка розничной цены и расчет скидок
-- Это примеры, замените 'Инструменты' на вашу группу товаров и задайте соответствующий процент
UPDATE Products SET retail_price = wholesale_price * 1.1 WHERE group_name = 'Инструменты'; -- 10% наценка для примера
UPDATE Products SET discount = 5 WHERE (retail_price - wholesale_price) / wholesale_price < 0.10;
UPDATE Products SET discount = 10 WHERE (retail_price - wholesale_price) / wholesale_price BETWEEN 0.10 AND 0.15;
UPDATE Products SET discount = 15 WHERE (retail_price - wholesale_price) / wholesale_price > 0.15;

-- Заполнение таблицы Наличие Товаров данными
INSERT INTO ProductAvailability (warehouse_number, product_code, quantity) VALUES
(1, 1, 500),
(2, 2, 300);
-- Добавьте остальные записи по аналогии
