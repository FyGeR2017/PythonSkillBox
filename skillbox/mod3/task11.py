k = int(input())
field = [list(input()) for _ in range(k)]


def check_line(line, symbol):
    return all(s == symbol for s in line)


for row in field:
    if check_line(row, 'X'):
        print('X')
        exit()
    elif check_line(row, 'O'):
        print('O')
        exit()

for i in range(k):
    line = [row[i] for row in field]
    if check_line(line, 'X'):
        print('X')
        exit()
    elif check_line(line, 'O'):
        print('O')
        exit()

line = [field[i][i] for i in range(k)]
if check_line(line, 'X'):
    print('X')
    exit()
elif check_line(line, 'O'):
    print('O')
    exit()

line = [field[i][k - i - 1] for i in range(k)][::-1]
if check_line(line, 'X'):
    print('X')
    exit()
elif check_line(line, 'O'):
    print('O')
    exit()

print('Ничья')