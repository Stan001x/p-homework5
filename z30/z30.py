a = int(input('Введите первое число списка: '))
b = int(input('Введите шаг арифметической прогрессии: '))
c = int(input('Введите количество элементов списка: '))

my_list = [a]

for i in range(1, c):
    my_list.append(my_list[i - 1] + b)
print(my_list)