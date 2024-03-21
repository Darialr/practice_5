year = int(input())
if (year % 100) % 4 == 0:
    print(366)
else:
    print(365)
