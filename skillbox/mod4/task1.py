numbers = input().split()

if len(set(numbers)) == len(numbers):
    print('Все числа разные')
elif len(set(numbers)) == 1:
    print('Все числа равны')
else:
    print('Есть равные и разные числа')
