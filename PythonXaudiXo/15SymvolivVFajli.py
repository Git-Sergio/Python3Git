filename = input('Вкажи який файл? : ')
file = open(filename, 'r')

print('В файлі "' + filename + '" : ' + str(len(file.read())) + ' символів' )

file.close()

# r - читання
# w -перезапись
# a - добавити в файл

# b -binary mode
