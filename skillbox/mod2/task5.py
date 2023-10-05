conditions = input()
symbol = conditions[0]
num = int(conditions[2:])       
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
