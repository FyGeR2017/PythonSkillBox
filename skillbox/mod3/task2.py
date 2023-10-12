num = int(input())
print(str(bin(num)[2:] + ', ' + oct(num)[2:] + ', ' + hex(num)[2:]) if num > 0 else 'Неверный ввод')