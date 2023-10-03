i = input('Символ: ')
n = int(input('Число: '))
count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lenght = len(alphabet)

for k in alphabet:
    count +=1
    if k == i:
        if count + n < lenght:
            print (alphabet[(count+n-1)%lenght])
        else: print(alphabet[(lenght-count+n-1)%lenght])
        
