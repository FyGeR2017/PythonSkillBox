coordinates = [0, 0]
step, count = 1, 1


def move(pos, x_or_y):
    global count
    for _ in range(step):
        coordinates[x_or_y] += pos
        if count == n:
            print(*coordinates)
            exit()
        count += 1


n = int(input('Кол-во шагов: '))
if n <= 0:
    print(*coordinates)
else:
    positions = str('ldru' * (n // 4 + 1))[:n]
    for ch in positions:
        if ch == 'l': move(-1, 0)
        elif ch == 'd':
            move(-1, 1)
            step += 1
        elif ch == 'r': move(1, 0)
        else:
            move(1, 1)
            step += 1