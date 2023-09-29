import random

my_tuple = tuple([random.randint(1, 100) for i in range(15)])
print(my_tuple)
print("Индекс максимального элемента: ", my_tuple.index(max(my_tuple)))
