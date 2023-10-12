size = int(input())

matrix = []
for i in range(size):
    row = []
    for j in range(1, size + 1):
        row.append(j)
    matrix.append(row)

print()
for row in matrix:print(*row)

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:print(*row)