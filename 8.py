kn = int(input('Введите количество кнатов: '))
gl = kn // (17*29)
skl = (kn % (17*29)) // 29
kn = (kn % (17*29)) % 29
if gl != 0:
    print(f'{gl} г.')
if skl != 0:
    print(f'{skl} с.')
if kn != 0:
    print(f'{kn} кн.')
