filename = input('Вкажи який файл? : ')
file = open(filename, 'r')
symvol = input('Вкажи кількість символів: ')
bite = file.read(int(symvol))
print('Виведено: ' + bite + ' Байт з '+ filename + ' файла')

file.close()

# r - читання
# w -перезапись
# a - добавити в файл

# b -binary mode
