string = input().lower()

vowels = "аеёийоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"

count_vowels = 0
count_consonants = 0

for i in string:
    if i in vowels:count_vowels+=1
print(count_vowels)

for j in string:
    if j in consonants:count_consonants+=1
print(count_consonants)
