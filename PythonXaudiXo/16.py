znach = input('Введіть ключ : ')

test = {
  'key1' : 'znachenia1',
  'key2' : {
    'in_key1' : 'in_znachenia1',
    },
  'k5' : 'znachenia5',
  125 : 'Сто двадцять пять',
  '33.55' : '33.55 znachenia'
}

if str(znach) in test:
  print('Є такий ключ str')

elif int(znach) in test:
  print('Є такий ключ int')

# elif float(znach) in test:
#   print('Є такий ключ float')

else:
  print('немає такого ключа')



