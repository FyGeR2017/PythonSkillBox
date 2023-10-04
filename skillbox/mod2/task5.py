conditions = input()
symbol = conditions[:conditions.find(',')]
num = int(conditions[conditions.find(',')+1:])         
count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lenght = len(alphabet)

for k in alphabet:
    count +=1
    if k == symbol:
        if count + num < lenght:
            print (alphabet[(count+num-1)%lenght])
        else: 
            print(alphabet[(lenght-count+num-1)%lenght])
