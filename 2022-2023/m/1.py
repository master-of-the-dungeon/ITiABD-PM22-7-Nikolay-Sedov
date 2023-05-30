class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position}), {self.age} years old"

class Teacher(Employee):
    def __init__(self, name, age, disciplines):
        super().__init__(name, age, "Teacher")
        self.disciplines = disciplines

    def add_dis(self, discipline):
        self.disciplines.append(discipline)

    def delete_dis(self, discipline):
        self.disciplines.remove(discipline)

    def __str__(self):
        return f"{super().__str__()} teaches: {', '.join(self.disciplines)}"

# Создание объекта класса Преподаватель
teacher = Teacher("Иванов Иван Иванович", 45, ["Математика", "Физика"])

# Вывод информации о преподавателе
print(teacher)

# Добавление новой дисциплины
teacher.add_dis("Информатика")

# Вывод обновленного списка дисциплин
print(teacher)

# Удаление дисциплины
teacher.delete_dis("Физика")

# Вывод обновленного списка дисциплин
print(teacher)
