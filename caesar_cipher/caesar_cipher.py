def selection_encrypted_letter(letter, encrypted_step, encrypted_alphabet):
    new_letter = ''
    double_alphabet = encrypted_alphabet * 2
    for current_letter in range(len(encrypted_alphabet)):
        if letter == encrypted_alphabet[current_letter]:
            new_letter = double_alphabet[current_letter + encrypted_step]
        if letter == ' ':
            new_letter = ' '
    return new_letter


message = list(input('Введите сообщение: '))

step = int(input('Введите сдвиг: '))

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

result = ''

for next_step in range(len(message)):
    next_letter = selection_encrypted_letter(message[next_step], step, alphabet)
    result += next_letter

print('Зашифрованное сообщение:', result)
