import random
# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(0,100) for student in names}


passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}