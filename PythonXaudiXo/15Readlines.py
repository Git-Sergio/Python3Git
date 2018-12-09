file =  open( 'sergio.py', 'r')

strings = file.readlines()

for string in strings:
  print( string )

file.close()
print('Файл прочитано!')
