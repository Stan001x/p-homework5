a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def sum(a, b):
    if a >= b:
        if a == 0:
            return 0
        if b <= 0:
            return 1 + sum(a-1, b-1)
        return 1 + 1 + sum(a-1, b-1)
    else:
        if b == 0:
            return 0
        if a <= 0:
            return 1 + sum(a-1, b-1)
        return 1 + 1 + sum(a-1, b-1)
print(sum(a, b))