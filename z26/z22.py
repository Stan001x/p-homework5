a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

def square(a, b):
    if b == 0:
        return 1
    return a * square(a, b-1)

print(square(a, b))
