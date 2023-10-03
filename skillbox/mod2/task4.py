def to_system(number, base):
  result = ''
  while number > 0:
    result = str(number % base) + result
    number //= base
  return int(result)

number = int(input('Введите число: '))

print(to_system(number, 2),to_system(number, 8),to_system(number, 16)) 
