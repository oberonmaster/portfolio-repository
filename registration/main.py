def logging_bad_registration(info, error_log):
    registrations_bad = open('registrations_bad.log', 'a', encoding='utf-8')
    registrations_bad.write(f'{info[:-1:]}...........{error_log}\n')
    registrations_bad.close()


with open('registrations.txt', 'r', encoding='utf=8') as registration_form:
    for line in registration_form:
        information = line.split()

        # количество полей с информацией
        try:
            if len(information) != 3:
                raise IndexError
        except IndexError:
            index_error_exception = 'НЕ присутствуют все три поля'
            logging_bad_registration(line, index_error_exception)
            continue

        # проверка на наличие только букв - первое поле
        try:
            if information[0].isalpha() is False:
                raise NameError
        except NameError:
            name_error_exception = 'поле имени содержит НЕ только буквы'
            logging_bad_registration(line, name_error_exception)
            continue

        # емейл содержит собаку - второе поле
        try:
            if information[1].count('@') != 1 or information[1].count('.') != 1:
                raise SyntaxError
        except SyntaxError:
            syntax_error_exception = 'Поле емейл НЕ содержит @ и .(точку)'
            logging_bad_registration(line, syntax_error_exception)
            continue

        # возраст от 10 до 99 лет - третье поле
        try:
            if int(information[2]) not in range(10, 99) or type(int(information[2])) != int:
                raise ValueError
        except ValueError:
            value_error_exception = 'поле возраст НЕ является числом от 10 до 99'
            logging_bad_registration(line, value_error_exception)
            continue

        else:
            registration_good = open('registrations_good.log', 'a', encoding='utf-8')
            registration_good.write(line)
            registration_good.close()
