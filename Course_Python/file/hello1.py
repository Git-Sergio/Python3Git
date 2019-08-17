f = open('test1.txt', 'r')
l = [line.strip() for line in f]
print(l)
f.read(10)
print ("Я на позиции:", f.tell())
# Возвращаемся в начало
f.seek(0)
print(f.read(10))

print("Имя файла: ", f.name)
print("В каком режиме файл открыт: ", f.mode)
# print("Пробелы: ", f.softspace)
print("Файл закрыт: ", f.closed)
f.close()
print("А теперь закрыт: ", f.closed)