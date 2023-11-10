import math

side = int(input("Введите сторону:"))


def triangle(side):
    perimetr = side * 3
    area = (math.sqrt(3) * side ** 2) / 4
    return perimetr, area


print("Сторона:", side)
result = triangle(side)
print("Периметр:", result[0], "Площадь:", result[1])
