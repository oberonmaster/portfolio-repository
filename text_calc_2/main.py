line_count = 0
final_result = 0

with open('calc_2.txt', 'r') as text_calc:  # правильный относительный путь к файлу
    for line in text_calc:
        split_line = line.split()
        line_count += 1

        # проверка на количество значений
        try:
            if len(split_line) != 3:
                raise ValueError
        except ValueError:
            print(f'Ошибка операции в строке {line_count} - неверное количество элементов')
            continue

        # проверка на целое число
        try:
            if int(split_line[0]):
                first_operand = int(split_line[0])
            else:
                raise ValueError
        except ValueError:
            print(f'Ошибка операции в строке {line_count} - '
                  f'первый операнд - {split_line[0]} - не является целым числом')
            continue

        try:
            if int(split_line[2]):
                second_operand = int(split_line[2])
            else:
                raise ValueError
        except ValueError:
            print(f'Ошибка операции в строке {line_count} - '
                  f'второй операнд - {split_line[2]} - не является целым числом')
            continue

        # проверка на операции
        while True:
            result = 0
            try:
                if split_line[1] == '/':
                    result = first_operand / second_operand
                    break
                elif split_line[1] == '*':
                    result = first_operand * second_operand
                    break
                elif split_line[1] == '-':
                    result = first_operand - second_operand
                    break
                elif split_line[1] == '+':
                    result = first_operand + second_operand
                    break
                elif split_line[1] == '%':
                    result = first_operand % second_operand
                    break
                else:
                    raise ValueError
            except ValueError:
                make_debug = input(f'Обнаружена ошибка в строке {line_count}: '
                                   f'{line[0:-1:]} Хотите исправить? ')
                if make_debug.lower() == 'да':
                    split_line = input('Введите исправленную строку: ').split()
                elif make_debug.lower() == 'нет':
                    break

        final_result += result

print(f'Сумма всех результатов составляет: {final_result}')
