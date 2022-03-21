import os


data = input('Введите строку: ')  # testiruyem

path_to_save = (input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')).split()
# path_to_save = 'D:/Skillbox/04_Python_Basic/Module22/05_save'

new_path = str()
for elem in path_to_save:
    new_path += os.path.join(os.path.sep, elem)

file_name = input('Введите имя файла: ')  # my_document

file = open(f'{file_name}.txt', 'w')

if os.path.exists(new_path):
    while True:
        answer = input('Вы действительно хотите перезаписать файл? (Да/Нет)').lower()
        if answer == 'да':
            file.write(data)
            print('Файл успешно сохранён!')
            break
        else:
            print('Ошибка! Файл не сохранен')
            file.close()
            break
else:
    file.write(data)
    print('Файл успешно сохранён!')
file.close()
