import sqlite3

def fetch_data(table_name):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Return both rows and column description
    return rows, cursor.description

def print_data(table_name):
    data, description = fetch_data(table_name)
    
    if not data:
        print(f"No data found in {table_name} table.")
        return

    # Print column names
    column_names = [desc[0] for desc in description]
    print(", ".join(column_names))

    # Print rows
    for row in data:
        print(row)

# Use the functions
print_data("Authors")
print("\n")
print_data("Publishers")
print("\n")
print_data("Books")
print("\n")
print_data("Warehouses")
print("\n")
print_data("Stock")
print("\n")
print_data("Customers")
print("\n")
print_data("ShoppingCarts")
print("\n")
print_data("CartItems")
print("\n")
print_data("Transactions")
