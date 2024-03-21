people_1 = int(input('Сколько подданных видели улыбку волшебницы за 1 день? '))
people_2 = int(input('Сколько подданных видели улыбку волшебницы за 2 день? '))
people_3 = int(input('Сколько подданных видели улыбку волшебницы за 3 день? '))
print('Количество повторений: ', end="")
if int(people_1 == people_2) + int(people_2 == people_3) == 2:
    print(3)
elif int(people_1 == people_2) + int(people_1 == people_3) + int(people_2 == people_3) == 1:
    print(2)
else:
    print(0)
