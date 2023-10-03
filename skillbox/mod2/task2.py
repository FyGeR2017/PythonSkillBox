side = int(input('сторона квадрата: '))

perimeter = side * 4
area = side ** 2
diagonal = round(side * (2**0.5),2)

print('Периметр:',perimeter,'\nПлощадь:', area,'\nДиагональ:', diagonal)
