groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Бадамшина",
        "exams": ["Программирование", "Базы данных", "Алгоритмы"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Соколова",
        "exams": ["Математика", "Физика", "Информатика"],
        "marks": [3, 4, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students_by_avg(group, threshold):
    filtered = []
    for student in group:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > threshold:
            filtered.append(student)
    return filtered

# Основной код
if __name__ == "__main__":
    threshold = float(input("Введите пороговое значение среднего балла: "))
    filtered_group = filter_students_by_avg(groupmates, threshold)
    print("\nСтуденты со средним баллом выше", threshold, ":")
    print_students(filtered_group)