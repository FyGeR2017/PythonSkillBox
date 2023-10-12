numbers = input().split()
print(True if len(set(numbers)) == len(numbers) else False)