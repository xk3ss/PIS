groupmates = [
    {
        "name": "Илья",
        "surname": "Костин",
        "exams": ["АиС", "ПИС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "Ин. яз.", "ИБ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["АиС", "Ин. яз.", "Web"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Сергей",
        "surname": "Михайлов",
        "exams": ["Информатика", "ПИС", "ИБ"],
        "marks": [4, 4, 3]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def filter_by_average(students, min_average):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_average:
            result.append(student)
    return result


threshold = float(input("Введите минимальный средний балл: "))
filtered = filter_by_average(groupmates, threshold)
print_students(filtered)
