import sqlite3

connection = sqlite3.connect("bookstore.db")
cursor = connection.cursor()

# Пример данных для Authors
cursor.executemany("""
INSERT INTO Authors (name, address, website)
VALUES (?, ?, ?)
""", [
    ("Лев Толстой", "1 ул. Ясная Поляна, Тула", "https://levtolstoy.ru"),
    ("Федор Достоевский", "2 ул. Карамазовых, Санкт-Петербург", "https://fdostoevsky.ru"),
])

# Пример данных для Publishers
cursor.executemany("""
INSERT INTO Publishers (name, address, phone_number, website)
VALUES (?, ?, ?, ?)
""", [
    ("Эксмо", "ул. Эксмо, Москва", "+74951234567", "https://eksmo.ru"),
    ("Азбука", "ул. Азбука, Санкт-Петербург", "+78129876543", "https://azbuka.ru"),
])

# Пример данных для Books
cursor.executemany("""
INSERT INTO Books (isbn, title, year, price, author_id, publisher_id)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    ("978-5-699-87677-5", "Война и мир", 1869, 1000.0, 1, 1),
    ("978-5-389-01289-0", "Преступление и наказание", 1866, 800.0, 2, 2),
])

# Пример данных для Warehouses
cursor.executemany("""
INSERT INTO Warehouses (address, phone_number)
VALUES (?, ?)
""", [
    ("ул. Складская 1, Москва", "+74957654321"),
    ("ул. Складская 2, Санкт-Петербург", "+78127654321"),
])

# Пример данных для Stock
cursor.executemany("""
INSERT INTO Stock (warehouse_id, isbn, quantity)
VALUES (?, ?, ?)
""", [
    (1, "978-5-699-87677-5", 50),
    (2, "978-5-699-87677-5", 30),
    (1, "978-5-389-01289-0", 40),
    (2, "978-5-389-01289-0", 20),
])

# Пример данных для Customers
cursor.executemany("""
INSERT INTO Customers (name, address, email, phone_number)
VALUES (?, ?, ?, ?)
""", [
    ("Иван Иванов", "ул. Иванова 1, Москва", "ivanov@email.ru", "+74951234567"),
    ("Анна Смирнова", "ул. Смирнова 2, Санкт-Петербург", "smirnova@email.ru", "+78129876543"),
])

# Пример данных для ShoppingCarts
cursor.executemany("""
INSERT INTO ShoppingCarts (customer_id)
VALUES (?)
""", [
    (1,),
    (2,),
])

# Пример данных для CartItems
cursor.executemany("""
INSERT INTO CartItems (cart_id, isbn, quantity)
VALUES (?, ?, ?)
""", [
    (1, "978-5-699-87677-5", 1),
    (2, "978-5-389-01289-0", 2),
])

# Пример данных для Transactions
cursor.executemany("""
INSERT INTO Transactions (cart_id, payment_address, delivery_address, delivery_method, credit_card_info)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, "ул. Иванова 1, Москва", "ул. Иванова 1, Москва", "Курьер", "1234-5678-9012-3456"),
    (2, "ул. Смирнова 2, Санкт-Петербург", "ул. Смирнова 2, Санкт-Петербург", "Почта", "9876-5432-1098-7654"),
])

connection.commit()
connection.close()
