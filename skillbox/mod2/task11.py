numbers = input()
unique = set()
for number in numbers:
  if number == ' ':
    continue
  if number in unique:
    print(False)
    break  
  unique.add(number)
else:
  print(True)
