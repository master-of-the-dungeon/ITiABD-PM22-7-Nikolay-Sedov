import sqlite3

connection = sqlite3.connect("bookstore.db")
cursor = connection.cursor()

# Authors table
cursor.execute("""
CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    website TEXT
)
""")

# Publishers table
cursor.execute("""
CREATE TABLE Publishers (
    publisher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    phone_number TEXT,
    website TEXT
)
""")

# Books table
cursor.execute("""
CREATE TABLE Books (
    isbn TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    price REAL,
    author_id INTEGER,
    publisher_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
)
""")

# Warehouses table
cursor.execute("""
CREATE TABLE Warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    address TEXT,
    phone_number TEXT
)
""")

# Stock table
cursor.execute("""
CREATE TABLE Stock (
    stock_id INTEGER PRIMARY KEY,
    warehouse_id INTEGER,
    isbn TEXT,
    quantity INTEGER,
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
    FOREIGN KEY (isbn) REFERENCES Books(isbn)
)
""")

# Customers table
cursor.execute("""
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    email TEXT,
    phone_number TEXT
)
""")

# ShoppingCarts table
cursor.execute("""
CREATE TABLE ShoppingCarts (
    cart_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

# CartItems table
cursor.execute("""
CREATE TABLE CartItems (
    cart_item_id INTEGER PRIMARY KEY,
    cart_id INTEGER,
    isbn TEXT,
    quantity INTEGER,
    FOREIGN KEY (cart_id) REFERENCES ShoppingCarts(cart_id),
    FOREIGN KEY (isbn) REFERENCES Books(isbn)
)
""")

# Transactions table - может быть дополнена позже на основе дополнительной информации
cursor.execute("""
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    cart_id INTEGER,
    payment_address TEXT,
    delivery_address TEXT,
    delivery_method TEXT,
    credit_card_info TEXT,
    FOREIGN KEY (cart_id) REFERENCES ShoppingCarts(cart_id)
)
""")

connection.commit()
connection.close()

