barcode = input()

even_sum = 0 #нечетные
odd_sum = 0 #четные

for i in range(len(barcode)):
    num = int(barcode[i])
    if i % 2 == 0: 
        odd_sum+=num
    else:
        even_sum+=num

if (odd_sum + even_sum * 3) % 10 == 0:print('yes')
else: print('no')
