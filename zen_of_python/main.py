result = []

zen_file = open('zen.txt', 'r')
for line in zen_file:
    result.insert(0, line)
for number, item in enumerate(result):
    if number == 0:
        result.remove(item)
        result.insert(0, str(item + '\n'))

result = ''.join(result)
print(result)
zen_file.close()

reverse_zen = open('reverse_zen.txt', 'w')
reverse_zen.write(result)
reverse_zen.close()
