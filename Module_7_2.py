def custom_write(file_name, strings):
    string_position = {}

    file = open(file_name, 'w', encoding = 'utf-8')
    for num_position, string in enumerate(strings, 1):
        num_bytes = file.tell()
        file.write(string + '\n')
        string_position[num_position, num_bytes] = string
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)