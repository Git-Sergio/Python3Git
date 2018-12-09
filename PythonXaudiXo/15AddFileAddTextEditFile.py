filename = input('Вкажи/Створи назву файлу  : ')
text = input('Який текст хочете добавити в файл ' + filename + ' :' )

file = open(filename, 'w')

file.write(text)

print('Текст записано!')

file.close()

# r - читання
# w -перезапись
# a - добавити в файл

# b -binary mode
