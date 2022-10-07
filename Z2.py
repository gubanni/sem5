with open('textZ2.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)


def compress(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for sim in text:
        if sim != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = sim
        else:
            count += 1
    enconding += str(count) + prev_char
    return enconding


text_compression = compress(my_text)

with open('textZ2compression.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)