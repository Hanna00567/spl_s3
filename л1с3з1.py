a = input("Ведите натуральное число ")
s = 0
for i in a:
    i = int(i)
    if i % 2 == 0:
        s += i
print(s)
