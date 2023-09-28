quarter1 = int(input('Введите сумму дохода за первый квартал: '))
quarter2 = int(input('Введите сумму дохода за второй квартал: '))
quarter3 = int(input('Введите сумму дохода за третий квартал: '))
quarter4 = int(input('Введите сумму дохода за четвёртый квартал: '))

sum1 = quarter1 + quarter2
sum2 = quarter3 + quarter4

growth_dynamics = sum1/sum2

print(growth_dynamics)
