num = int(input())
if 10 < num < 20 or num % 10 == 0:
    print('попугаев')
elif num % 10 == 1:
    print('попугай')
elif 2 <= num % 10 <= 4:
    print('попугая')
else:
    print('попугаев')
