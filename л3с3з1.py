with open('F1.txt', 'w+') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения):")
        if not line:
            break
        f1.write(line + '\n')
    f1.seek(0)
    cont=f1.readlines()
    print(cont)

with open('F1.txt', 'r+') as f1:
    with open('F2.txt', 'w+') as f2:
        for line in f1:
            if line.endswith('A\n'):
                f2.write(line)

with open('F2.txt', 'r+') as f2:
    f2.seek(0)
    content = f2.read()
    if content:
        print("\nСодержание файла F2:")
        print(content)
    else:
        print("\nФайл F2 пуст.")

print("Программа завершена. Строки, заканчивающиеся на 'A', скопированы в файл F2.")
