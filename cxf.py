import random

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

new_students_name = "Назар"
new_students = {
    "Пошта": "Nazar@gmail.com",
    "Вік": random.randint(18, 40),
    "Номер телефону": "+380986523556",
    "Середній бал": random.uniform(0, 100)
}

students[new_students_name] = new_students

average_group_score = sum(student["Середній бал"] for student in students.values()) / len(students)

for student in students.values():
    if student["Номер телефону"] is None:
        student["Номер телефону"] = '+380961231234'