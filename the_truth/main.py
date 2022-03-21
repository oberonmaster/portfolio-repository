def cesar_cipher(letter, encrypted_step, encrypted_alphabet):
    new_letter = ''
    double_alphabet = encrypted_alphabet * 2
    for current_letter in range(len(encrypted_alphabet)):
        if letter == encrypted_alphabet[current_letter]:
            new_letter = double_alphabet[current_letter + encrypted_step]
        if letter == ' ':
            new_letter = ' '
    return new_letter


def step_cipher(word, step):
    if len(word) < step:
        new_step = step % len(word) # компенсация когда слово короче шага
    else:
        new_step = step
    part_1 = str(word[0: -new_step:])
    part_2 = str(word[-new_step::])
    result = part_2 + part_1
    return result

message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
message = message.lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# учет символов при последующем смещении
formated_message = ''
for symbol in message:
    if symbol.isalpha() is False and symbol != ' ' and symbol != '/': # and symbol != '"' and symbol != '.' and symbol != '(' and symbol != '+':
        symbol = '0'
    formated_message += symbol

# print(formated_message)

# step part
splited_message = formated_message.split()
returned_message = []
correction_step = 0
for word in splited_message:
    if '/' in word:
        correction_step += 1
    step_result = step_cipher(word, 3 + correction_step) #шаг определил по большой букве
    returned_message.append(step_result)

returned_message = str(returned_message)
# print(returned_message)

# cesar part
cesar_cipher_result = ''
cesar_cipher_step = -1 #подобрал методом тыка
for next_step in range(len(returned_message)):
    next_letter = cesar_cipher(returned_message[next_step], cesar_cipher_step, alphabet)
    cesar_cipher_result += next_letter

print(cesar_cipher_result)