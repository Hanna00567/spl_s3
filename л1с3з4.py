my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}

# Находим ключи с наименьшими значениями
min_values = sorted(my_dict, key=my_dict.get)[:3]

print(min_values)
