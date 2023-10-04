numbers = input()
a, b = int(numbers[:numbers.find(',')]), int(numbers[numbers.find(' ')+1:])
print(a%b)
