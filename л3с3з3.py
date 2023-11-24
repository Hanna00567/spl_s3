file_path ="subjects.txt"
subjects_dict={}

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(":")
            if len(parts) == 2:
                subject_name=parts[0].strip()
                lessons_info=parts[1].strip().split()

                total_lessons = 0
                for lesson in lessons_info:
                    lesson_count = lesson.split("(")
                    if len(lesson_count) == 2:
                        total_lessons += int(lesson_count[0])

                subjects_dict[subject_name] = total_lessons
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")

print("Словарь с общим количеством занятий по предметам:")
print(subjects_dict)