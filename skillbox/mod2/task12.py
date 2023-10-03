number = input()
clean_number = ''
numbers = '+0123456789'

for char in number:
    if char in numbers:
        clean_number += char
print(clean_number)
