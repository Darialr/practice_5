pin = int(input('Введите PIN-код: '))
n1 = (pin % 10000) // 1000
n2 = (pin % 1000) // 100
n3 = (pin % 100) // 10
n4 = pin % 10
if 1900 <= pin <= 2050:
    print('ERROR')
elif pin // 1000 == 0 or pin // 1000 > 9:
    print('ERROR')
elif n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print('ERROR')
else:
    print('OK')
