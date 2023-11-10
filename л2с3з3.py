n, m = map(int, input().split())
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)
i, j = map(int, input().split())
for row in array:
    row[i], row[j] = row[j], row[i]
for row in array:
    print(*row)
