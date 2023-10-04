a, b, c = map(int, input('введите три числа через пробел: ').split())

numbers = [a, b, c]
for n in numbers:
  if n <= -1000 or n >= 1000:
    print('число вне диапазона')
    break
else:
  numbers.sort()
  print(numbers[1])
