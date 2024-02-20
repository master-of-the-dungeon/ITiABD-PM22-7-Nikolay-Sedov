import sqlite3
import matplotlib.pyplot as plt

def fetch_data():
    conn = sqlite3.connect('wholesale_store.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT s.name, SUM(p.selling_price - p.purchase_price) * sa.quantity as profit, SUM(p.selling_price * sa.quantity * s.commission_percent) as commission
    FROM sales sa
    JOIN products p ON sa.product_id = p.id
    JOIN sellers s ON sa.seller_id = s.id
    GROUP BY sa.seller_id
    ''')

    data = cursor.fetchall()
    conn.close()
    return data

def plot_data(data):
    sellers = [row[0] for row in data]
    profits = [row[1] for row in data]
    commissions = [row[2] for row in data]

    x = range(len(sellers))

    plt.bar(x, profits, width=0.4, label="Profit", align='center', alpha=0.7)
    plt.bar(x, commissions, width=0.4, label="Commission", align='edge', alpha=0.7)

    plt.xlabel('Sellers')
    plt.ylabel('Amount ($)')
    plt.xticks(x, sellers)
    plt.title('Profits and Commissions by Seller')
    plt.legend()
    plt.tight_layout()

    plt.show()

data = fetch_data()
plot_data(data)
