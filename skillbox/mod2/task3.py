numbers = input()

a = int(numbers[:numbers.find(' ')])
b = int(numbers[numbers.find(' ')+1:numbers.rfind(' ')])
c = int(numbers[numbers.rfind(' ')+1:])

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

