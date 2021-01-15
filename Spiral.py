size = int(input())
n = size  # размер квадрата
a = 0  # смещение от левого верхнего угла
b = 1  # число
#  создаем матрицу наполненную нулями
arr = [[0 for j in range(size)] for i in range(size)]

while n > 0:
    if n != 1:
        for i in range(n-1):
            arr[a - size][i + a] = b
            b += 1
        for j in range(n-1):
            arr[j + a][size - 1 - a] = b
            b += 1
        for i in range(n - 1, -1, -1):
            arr[size - 1 - a][i + a] = b
            b += 1
        for j in range(n - 2, 0, -1):
            arr[j + a][a - size] = b
            b += 1
    else:
        arr[a][a] = b
    a += 1
    n -= 2

#  Вывод
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
