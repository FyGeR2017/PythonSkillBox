string = input() + ' '
word = ''

for char in string:
    if char == ' ': word+=last_char
    last_char = char
    
print(word)
    
