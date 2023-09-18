import sqlite3
import matplotlib.pyplot as plt

def fetch_data():
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT r.name, SUM(p.price * r.commission_percent) as commission
    FROM transactions t
    JOIN properties p ON t.property_id = p.id
    JOIN realtors r ON t.realtor_id = r.id
    GROUP BY t.realtor_id
    ''')

    data = cursor.fetchall()
    conn.close()
    return data

def plot_data(data):
    realtors = [row[0] for row in data]
    commissions = [row[1] for row in data]

    x = range(len(realtors))

    plt.bar(x, commissions, width=0.4, align='center', alpha=0.7, color='skyblue')

    plt.xlabel('Realtors')
    plt.ylabel('Commission ($)')
    plt.xticks(x, realtors)
    plt.title('Commissions by Realtor')
    plt.tight_layout()

    plt.show()

data = fetch_data()
plot_data(data)
