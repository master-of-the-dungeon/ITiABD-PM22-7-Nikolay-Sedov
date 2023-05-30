class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGroup: {self.group}")

    def is_searched(self, search_name):
        return self.name == search_name


class Aspirant(Student):
    def __init__(self, name, age, group, supervisor):
        super().__init__(name, age, group)
        self.supervisor = supervisor

    def display_info(self):
        super().display_info()
        print(f"Supervisor: {self.supervisor}")


class Bachelor(Student):
    def __init__(self, name, age, group, thesis_topic):
        super().__init__(name, age, group)
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")

# Создаем список студентов
students = [
    Aspirant("Иван", 27, "A1", "Пупкин Василий Сергеевич"),
    Bachelor("Яна", 21, "B2", "Эмуляция процесса пивоварения"),
    Student("Вова", 20, "A2"),
    Aspirant("Алиса", 26, "C1", "Ганибал Лектер"),
    Bachelor("Ашот", 22, "B1", "Использование песен Ольги Бузовой в качестве звукового оружия"),
]


for student in students:
    student.display_info()
    print()


search_name = "Ашот"
for student in students:
    if student.is_searched(search_name):
        print(f"{search_name} is found!")
        break
else:
    print(f"{search_name} is not found.")
