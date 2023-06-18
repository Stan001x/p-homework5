import random

my_list = [random.randint(0, 100) for _ in range(20)]

print(my_list)

minn = int(input('Введите минимальное значение диапазона: '))
maxx = int(input('Введите максимальное значение диапозона: '))
indexlist = list()
for i in range(len(my_list)):
    if minn<=my_list[i]<=maxx:
        indexlist.append(i)
print(indexlist)