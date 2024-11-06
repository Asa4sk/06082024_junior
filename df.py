# Initial dictionary of students
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

import random

# 1. Add a new student
new_student_name = 'Олена Литвин'
new_student = {
    'Пошта': 'Olena@gmail.com',
    'Вік': random.randint(18, 40),  # Random age between 18 and 40
    'Номер телефону': '+380971231234',  # Assigned phone number
    'Середній бал': round(random.uniform(0, 100), 2)  # Random average score between 0 and 100
}

students[new_student_name] = new_student

# 2. List of students with average score > 90
high_score_students = {name: info for name, info in students.items() if info['Середній бал'] > 90}

# 3. Calculate the average score for the group
average_group_score = sum(student['Середній бал'] for student in students.values()) / len(students)

# 4. Add parents' phone number if student's phone is missing
for student in students.values():
    if student['Номер телефону'] is None:
        student['Номер телефону'] = '+380961231234'  # Parent's phone number

# Output all results
students, high_score_students, average_group_score