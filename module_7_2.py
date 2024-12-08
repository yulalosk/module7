def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        bb = 0
        strings_positions = {}
        for pos, string in enumerate(strings,start=1):
            file.write(string + '\n')
           # pos += 1
           # - len(string)
            strings_positions[(pos,bb)] = string
            bb = file.tell()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for key, value in result.items():
    print(key, value)