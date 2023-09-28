number = int(input('Введите четырёхзначное число: '))

first = number // 1000
second = (number // 100) % 10
third = (number % 100) // 10
fourth = number %10

print(first)
print(second)
print(third)
print(fourth)
