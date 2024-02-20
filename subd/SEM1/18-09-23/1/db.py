import sqlite3


def create_tables():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    # Создание таблицы Patients
    cursor.execute('''CREATE TABLE IF NOT EXISTS Patients (
                        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_name TEXT NOT NULL)''')

    # Создание таблицы Doctors
    cursor.execute('''CREATE TABLE IF NOT EXISTS Doctors (
                        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        specialty TEXT NOT NULL,
                        cost_of_appointment REAL NOT NULL,
                        percentage_of_salary REAL NOT NULL)''')

    # Создание таблицы Appointments
    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        doctor_id INTEGER,
                        appointment_date TEXT NOT NULL,
                        receipt_number TEXT,
                        salary_paid REAL,
                        FOREIGN KEY(patient_id) REFERENCES Patients(patient_id),
                        FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id))''')

    conn.commit()
    conn.close()


def add_patient(name):
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Patients (patient_name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def add_doctor(specialty, cost, percentage):
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Doctors (specialty, cost_of_appointment, percentage_of_salary) VALUES (?, ?, ?)",
                   (specialty, cost, percentage,))
    conn.commit()
    conn.close()


def calculate_salary(cost, percentage):
    salary = cost * (percentage / 100)
    tax = 0.13 * salary
    return salary - tax


def add_appointment(patient_id, doctor_id, date):
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    # Получение информации о враче
    cursor.execute("SELECT cost_of_appointment, percentage_of_salary FROM Doctors WHERE doctor_id=?", (doctor_id,))
    doctor_data = cursor.fetchone()

    if doctor_data:
        cost = doctor_data[0]
        percentage = doctor_data[1]
        salary = calculate_salary(cost, percentage)

        # Создание квитанции (можно улучшить формат квитанции)
        receipt_number = f"REC-{doctor_id}-{patient_id}-{date}"

        cursor.execute(
            "INSERT INTO Appointments (patient_id, doctor_id, appointment_date, receipt_number, salary_paid) VALUES (?, ?, ?, ?, ?)",
            (patient_id, doctor_id, date, receipt_number, salary,))
        conn.commit()

    conn.close()


create_tables()  # Создание таблиц
# Добавление пациентов
patients = ["John Doe", "Jane Smith", "Robert Brown", "Emily Davis", "William Wilson"]
for patient in patients:
    add_patient(patient)

# Добавление врачей
doctors = [
    ("Cardiologist", 100.0, 70),
    ("Surgeon", 150.0, 80),
    ("Ophthalmologist", 80.0, 60),
    ("Therapist", 90.0, 65)
]
doctor_names = ["Dr. Steven Clark", "Dr. Angela Garcia", "Dr. Raymond Rodriguez", "Dr. Dorothy White"]

for idx, (specialty, cost, percentage) in enumerate(doctors):
    add_doctor(f"{doctor_names[idx]} ({specialty})", cost, percentage)

# Добавление приемов
appointments = [
    (1, 1, "2023-09-18"),
    (2, 2, "2023-09-20"),
    (3, 4, "2023-09-22"),
    (4, 3, "2023-09-23"),
    (5, 1, "2023-09-25")
]

for patient_id, doctor_id, date in appointments:
    add_appointment(patient_id, doctor_id, date)
# Примеры добавления записей
add_patient("John Doe")
add_doctor("Cardiologist", 100.0, 70)  # Кардиолог с стоимостью приема $100 и 70% зарплаты от этой стоимости
add_appointment(1, 1, "2023-09-18")
