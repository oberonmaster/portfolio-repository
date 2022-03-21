import zipfile

v_i_m = zipfile.ZipFile('voyna-i-mir.zip')
v_i_m.extractall()

v_i_m_text = open('voyna-i-mir.txt', 'r', encoding='utf-8')

collect = dict()

for line in v_i_m_text:
    for word in line:
        if word.isalpha():
            if word in collect:
                collect[word] += 1
            else:
                collect[word] = 1

sorted_collect = sorted(collect.items(), key=lambda x: x[1], reverse=True)

sorted_result = dict()
for element in sorted_collect:
    sorted_result[element[0]] = element[1]

print(sorted_result)

v_i_m_text.close()
v_i_m.close()


