import random

students = ['A', 'B', 'C', 'D', 'F']
student_scores = {name:random.randint(0, 100) for name in students}

passed_students = {name:grade for (name, grade) in student_scores.items() if grade >= 50}

print(passed_students)
