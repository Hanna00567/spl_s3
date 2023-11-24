def read_student_data(file_path):
    students = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                surname, average_score = parts
                students.append((surname, float(average_score)))
    return students


def filter_students_by_score(students, min_score, max_score):
    filtered_students = [student for student in students if min_score <= student[1] <= max_score]
    return filtered_students


def find_max_score_student(students):
    max_student = max(students, key=lambda x: x[1])
    return max_student


file_path = "students.txt"
student_data = read_student_data(file_path)

low_score_students = filter_students_by_score(student_data, 4, 6)
medium_score_students = filter_students_by_score(student_data, 6, 8)
high_score_students = filter_students_by_score(student_data, 8, float('inf'))

print("Студенты со средним баллом от 4 до 6:")
for student in low_score_students:
    print(student[0])

print("\nСтуденты со средним баллом от 6 до 8:")
for student in medium_score_students:
    print(student[0])

print("\nСтуденты со средним баллом выше 8:")
for student in high_score_students:
    print(student[0])

max_score_student = find_max_score_student(student_data)
print("\nСтудент с максимальным средним баллом:", max_score_student[0], "с баллом", max_score_student[1])
