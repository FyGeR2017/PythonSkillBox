domain = input()
parts = domain.split('.')
parts.reverse()

for part in parts:
  print(part)
