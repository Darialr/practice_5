num = int(input())
if num % 10 == (num % 10000) // 1000 and (num % 100) // 10 == (num % 1000) // 100:
    print('настоящее')
else:
    print('кривое')
