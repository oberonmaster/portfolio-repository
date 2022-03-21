def cesar_cipher(text, step):
    text = text.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    result = str()
    for word in text:
        for number, _ in enumerate(alphabet):
            if word == alphabet[number]:
                result += alphabet[(number + step) % len(alphabet)]
    result = result.title()
    result += '\n'
    return result


text_file = open('text.txt', 'r')
# text_file.write('Hello\nHello\nHello\nHello')
result_file = open('cipher_text.txt', 'w')

count = 0
for item in text_file:
    count += 1
    result_file.write(cesar_cipher(item, count))

text_file.close()
result_file.close()
