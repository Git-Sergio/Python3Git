#Програма для копіювання файлів!

filename1 = input('Який файл забекапити?: ')
filename2 = 'backup_' + filename1

file1 =  open(filename1, 'rb')
file2 =  open(filename2, 'wb')  # 'ab'

file2.write( file1.read() )

file1.close()
file2.close()
print('Бекап файлу зроблено!')
