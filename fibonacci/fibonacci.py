def fibonacci_value(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci_value(position - 1) + fibonacci_value(position - 2)


target = int(input('Введите позицию числа в ряде Фибоначчи: '))

print(fibonacci_value(target))
