list = [12, 511, 'Python', 311, 122, 'love']

for i in list:
    if isinstance(i, int):
        if i % 2 == 0:
            k = str(i)
            sum = 0
            for j in k:
                sum += int(j)
            list[list.index(i)] = sum
        else:
            list[list.index(i)] = 1

print(list)
