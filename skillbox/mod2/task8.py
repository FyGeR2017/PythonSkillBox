string = input('')
i = input('')
count = 0

for j in string:
    if j == i:
        count += 1
    else:        
        break

print(count)
