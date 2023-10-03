string = input('')

one = 0
zero = 0

for i in string:
    if i == '1':one+=1
    else: zero+=1

if one == zero: print('yes')
else: print('no')
