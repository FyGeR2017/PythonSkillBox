word = input("Введите слово: ")

letters = {}

for letter in word:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

odd_count = 0
one_letter = 0

for count in letters.values():
    if count % 2 != 0:
        odd_count += 1

if odd_count > 1:
    print("Нельзя составить палиндром")
else:
    print("Можно составить палиндром")