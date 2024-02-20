import sqlite3

# Функция для добавления данных в таблицу Publications
def insert_publications():
    conn = sqlite3.connect("university_library.db")
    cursor = conn.cursor()
    
    # Вставляем данные в таблицу Publications
    publications = [
        ('001', 'Книга 1', 'Автор 1', 'Книга', 30, 'Город 1', 'Издательство 1', 2020, 200, '1234567890', 100, 100, 0),
        ('002', 'Книга 2', 'Автор 2', 'Книга', 30, 'Город 2', 'Издательство 2', 2019, 250, '2345678901', 150, 150, 0),
        # Добавьте другие издания
    ]
    
    cursor.executemany("""
    INSERT INTO Publications (code, title, author, type, read_duration, city, publisher, publication_year, num_pages, isbn, total_copies, available_copies, issue_for_year)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, publications)
    
    conn.commit()

# Функция для добавления данных в таблицу Readers
def insert_readers():
    conn = sqlite3.connect("university_library.db")
    cursor = conn.cursor()
    
    # Вставляем данные в таблицу Readers
    readers = [
        ('Студент', 'Иван Иванов', '+1234567890', '1990-01-01', 'LIB-001', 'STU-001', 1, 'Департамент 1', 'Факультет 1'),
        ('Преподаватель', 'Петр Петров', '+2345678901', '1985-03-15', 'LIB-002', 'STU-002', None, 'Департамент 2', 'Факультет 2'),
        # Добавьте других читателей
    ]
    
    cursor.executemany("""
    INSERT INTO Readers (category, full_name, phone_number, date_of_birth, library_card_number, student_card_number, grade, department, faculty)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, readers)
    
    conn.commit()

# Функция для добавления данных в таблицу PublicationPackages
def insert_publication_packages():
    conn = sqlite3.connect("university_library.db")
    cursor = conn.cursor()
    
    # Вставляем данные в таблицу PublicationPackages
    packages = [
        ('Пакет 1', 2023),
        ('Пакет 2', 2023),
        # Добавьте другие пакеты
    ]
    
    cursor.executemany("""
    INSERT INTO PublicationPackages (package_name, year)
    VALUES (?, ?)
    """, packages)
    
    conn.commit()

# Функция для добавления данных в таблицу Users
def insert_users():
    conn = sqlite3.connect("university_library.db")
    cursor = conn.cursor()
    
    # Вставляем данные в таблицу Users
    users = [
        ('Администратор', 'admin', 'admin_password'),
        ('Методист', 'methodist', 'methodist_password'),
        ('Библиотекарь', 'librarian', 'librarian_password'),
    ]
    
    cursor.executemany("""
    INSERT INTO Users (role, username, password)
    VALUES (?, ?, ?)
    """, users)
    
    conn.commit()

# Вызываем функции для добавления данных в таблицы
insert_publications()
insert_readers()
insert_publication_packages()
insert_users()

print("Данные успешно добавлены в базу данных.")
