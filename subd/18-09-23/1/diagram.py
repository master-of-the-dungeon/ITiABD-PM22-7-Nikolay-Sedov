import matplotlib.pyplot as plt
import sqlite3

def plot_salary_distribution():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    # Запрашиваем зарплату каждого врача, суммированную по всем приемам
    cursor.execute('''SELECT d.specialty, SUM(a.salary_paid) 
                      FROM Doctors d
                      JOIN Appointments a ON d.doctor_id = a.doctor_id
                      GROUP BY d.specialty''')

    data = cursor.fetchall()
    conn.close()

    # Разбиваем данные на специальности и суммы зарплат
    specialties, salaries = zip(*data)

    # Построение диаграммы
    plt.bar(specialties, salaries, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Specialty')
    plt.ylabel('Total Salary Paid')
    plt.title('Salary Distribution by Doctor Specialty')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# После добавления данных вызываем функцию вывода диаграммы
plot_salary_distribution()
