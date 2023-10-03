a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a > b:
  if b > c:
    print(b)
  else:
    if a > c:
      print(c)  
    else:
      print(a)
else:
  if a > c:
    print(a)
  else:
    if b > c:
      print(c)
    else:
      print(b)
      
if a < -1000 or a > 1000:
  print('Число a вне диапазона')
elif b < -1000 or b > 1000:  
  print('Число b вне диапазона') 
elif c < -1000 or c > 1000:
  print('Число c вне диапазона')
