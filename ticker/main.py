def finding_step(word):
    part_1 = str(word[0:-1:])
    part_2 = str(word[-1::])
    result = part_2 + part_1
    return result


first_message = 'abcd'  # input('Первая строка: ')
second_message = 'cdba'  # input('Вторая строка: ')

count = 0

for _ in range(len(first_message)):
    if first_message != second_message:
        second_message = finding_step(second_message)
        count += 1
    elif first_message == second_message:
        output_message = f'Первая строка получается из второй со сдвигом {count}.'
        print(output_message)
        break

if first_message != second_message:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
