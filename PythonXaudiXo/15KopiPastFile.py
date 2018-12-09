#Програма для копіювання файлів!

filename1 = input('Введіть назву копійованого файлу: ')
filename2 = input('Введіть куди скопіювати файл?: ')

file1 =  open(filename1, 'r')
file2 =  open(filename2, 'w') # 'a'добавити до існуючого

file2.write( file1.read() )

file1.close()
file2.close()
print('Копіювання завершено!')
