filename = input('Вкажи який файл? : ')
text = input('Який текст додати? : ')

file = open(filename, 'a')
file.write(text)

print('Текст додано в файл: ' + filename )

file.close()

# r - читання
# w -перезапись
# a - добавити в файл

# b -binary mode
