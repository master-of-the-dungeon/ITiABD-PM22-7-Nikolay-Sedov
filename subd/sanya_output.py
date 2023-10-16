import sqlite3
from prettytable import PrettyTable

def fetch_and_display_data(table_name):
    conn = sqlite3.connect("university_library.db")
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print(f"No data found in the '{table_name}' table.")
    else:
        columns = [desc[0] for desc in cursor.description]
        table = PrettyTable(columns)
        
        for row in rows:
            table.add_row(row)
        
        print(table)
    
    conn.close()

# Пример вывода данных из таблицы Publications
fetch_and_display_data("Publications")

# Пример вывода данных из других таблиц
# fetch_and_display_data("Readers")
# fetch_and_display_data("PublicationPackages")
# fetch_and_display_data("Users")
