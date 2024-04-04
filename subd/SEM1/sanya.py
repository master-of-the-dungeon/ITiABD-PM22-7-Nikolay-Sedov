import sqlite3

# Создаем или подключаемся к базе данных (если файл не существует, он будет создан)
conn = sqlite3.connect("university_library.db")
cursor = conn.cursor()

# Создаем таблицу для изданий
cursor.execute("""
CREATE TABLE IF NOT EXISTS Publications (
    id INTEGER PRIMARY KEY,
    code TEXT,
    title TEXT,
    author TEXT,
    type TEXT,
    read_duration INTEGER,
    city TEXT,
    publisher TEXT,
    publication_year INTEGER,
    num_pages INTEGER,
    isbn TEXT,
    total_copies INTEGER,
    available_copies INTEGER,
    issue_for_year INTEGER
)
""")

# Создаем таблицу для читателей
cursor.execute("""
CREATE TABLE IF NOT EXISTS Readers (
    id INTEGER PRIMARY KEY,
    category TEXT,
    full_name TEXT,
    phone_number TEXT,
    date_of_birth TEXT,
    library_card_number TEXT,
    student_card_number TEXT,
    grade INTEGER,
    department TEXT,
    faculty TEXT
)
""")

# Создаем таблицу для пакетов изданий
cursor.execute("""
CREATE TABLE IF NOT EXISTS PublicationPackages (
    id INTEGER PRIMARY KEY,
    package_name TEXT,
    year INTEGER
)
""")

# Создаем таблицу для связи читателей и изданий (выдача изданий)
cursor.execute("""
CREATE TABLE IF NOT EXISTS BookLending (
    id INTEGER PRIMARY KEY,
    reader_id INTEGER,
    publication_id INTEGER,
    issue_date TEXT,
    due_date TEXT,
    status TEXT
)
""")

# Создаем таблицу для пользователей (администратор, методист, библиотекарь)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    role TEXT,
    username TEXT,
    password TEXT
)
""")

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных 'university_library.db' создана успешно.")
