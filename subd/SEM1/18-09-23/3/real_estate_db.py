import sqlite3

# Инициализация базы данных
conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS properties (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS realtors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    commission_percent REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    realtor_id INTEGER,
    property_id INTEGER,
    transaction_date TEXT,
    FOREIGN KEY (realtor_id) REFERENCES realtors(id),
    FOREIGN KEY (property_id) REFERENCES properties(id)
)
''')

# Заполнение данными
properties = [
    ('123 Main St', 200000),
    ('456 Elm St', 250000),
    ('789 Maple St', 180000),
    ('101 Pine St', 220000),
    ('110 Oak St', 270000),
    ('245 Birch St', 300000),
    ('309 Cherry St', 260000),
    ('512 Redwood St', 235000),
    ('687 Spruce St', 190000),
    ('785 Cedar St', 205000)
]

realtors = [
    ('Alice', 0.03),
    ('Bob', 0.025),
    ('Charlie', 0.02),
    ('David', 0.04),
    ('Eve', 0.03),
    ('Frank', 0.035),
    ('Grace', 0.028)
]

transactions = [
    (1, 1, '2023-09-18'),
    (2, 2, '2023-09-19'),
    (3, 3, '2023-09-20'),
    (1, 4, '2023-09-21'),
    (5, 5, '2023-09-22'),
    (6, 6, '2023-09-23'),
    (4, 7, '2023-09-24'),
    (2, 8, '2023-09-25'),
    (3, 9, '2023-09-26'),
    (7, 10, '2023-09-27')
]

cursor.executemany('INSERT INTO properties (address, price) VALUES (?, ?)', properties)
cursor.executemany('INSERT INTO realtors (name, commission_percent) VALUES (?, ?)', realtors)
cursor.executemany('INSERT INTO transactions (realtor_id, property_id, transaction_date) VALUES (?, ?, ?)', transactions)

conn.commit()
conn.close()
