str = input("Введите строку: ")
counter = 0
list = []
podstr = ''
for i in str:
    if i.isdigit():
        podstr += i
        counter += 1
else:
    if podstr:
        list.append(podstr)
        podstr = ''
if podstr:
    list.append(podstr)
if counter == 0:
    print("Нет чисел в строке")
else:
    print("Количество чисел: ", len(list))
