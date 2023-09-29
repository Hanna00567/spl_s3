text = input("Введите текст: ").lower()
vowels = ['а', 'ё', 'у', 'е', 'ы', 'о', 'я', 'и', 'ю', 'ё']
consonants = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'м', 'т', 'б', 'с',
              'ь', 'ъ']
vowels_count = 0
consonants_count = 0
for char in text:
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1


if vowels_count == consonants_count:
    print("Гласные буквы в тексте:", ', '.join([char for char in text if char in vowels]))
    words = text.split()
    print("Количество слов в тексте:", len(words))
    print("Количество гласных букв:", vowels_count)
    print("Количество согласных букв:", consonants_count)
elif vowels_count != consonants_count:
    words = text.split()
    print("Количество слов в тексте:", len(words))
    print("Количество гласных букв:", vowels_count)
    print("Количество согласных букв:", consonants_count)