import sqlite3

# Инициализация базы данных
conn = sqlite3.connect('wholesale_store.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    purchase_price REAL NOT NULL,
    selling_price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sellers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    commission_percent REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    seller_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (seller_id) REFERENCES sellers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
''')

# Дополнительные продукты
extra_products = [
    ('Fig', 1.2, 2.4),
    ('Grape', 0.8, 1.6),
    ('Honeydew', 3.0, 6.0),
    ('Iced Tea', 0.6, 1.2),
    ('Jackfruit', 2.5, 5.0),
    ('Kiwi', 0.9, 1.8),
    ('Lemon', 0.4, 0.9),
    ('Mango', 2.0, 4.5)
]

# Дополнительные продавцы
extra_sellers = [
    ('Eve', 0.03),
    ('Frank', 0.02),
    ('Grace', 0.05),
    ('Hannah', 0.04)
]

# Дополнительные продажи
extra_sales = [
    (4, 5, 4),
    (5, 6, 3),
    (3, 7, 6),
    (4, 8, 5),
    (2, 9, 10),
    (1, 10, 12),
    (6, 11, 7),
    (7, 12, 15)
]

# Добавляем дополнительные данные в таблицы
cursor.executemany('INSERT INTO products (name, purchase_price, selling_price) VALUES (?, ?, ?)', extra_products)
cursor.executemany('INSERT INTO sellers (name, commission_percent) VALUES (?, ?)', extra_sellers)
cursor.executemany('INSERT INTO sales (seller_id, product_id, quantity) VALUES (?, ?, ?)', extra_sales)

conn.commit()
conn.close()