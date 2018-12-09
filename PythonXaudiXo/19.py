# Форматування строк .format() /   % /  Konkotynacja

#Konkotynacja
name = 'Tymon'
age = 3
print('Pryvit, ' + str(name) + '!\nTobi vze ' + str(age) + ' rokiv')


# Форматування строк %
#в стиль printf
name = 'Mariana'
age = 31
print('Pryvit, %s!\nTobi vze %d rokiv' % (name, age))
# %s -Плейсхолдер строки str
# %d -Плейсхолдер числа int
# %f -Плейсхолдер дроби float


# Форматування строк .format()
name = 'Sergio'
age = 35
print('Pryvit, {}!\nTobi vze {} rokiv' .format(name, age))
print('Pryvit, {0}!\nTebe uze {1} rokiv' .format(name, age))

#pruklad
print('{0}{1}{0}' .format('abra','cad'))

#
person_name = 'Maty'
person_age = 5
print('Pryvit, {name}!\nTobi vze {age} rokiv' .format(name = person_name, age = person_age))

#Формат
person = {
    'name': 'Bob',
    'age' : 33
    }
print('Імя: {name}\nВік: {age}'.format( name = person['name'], age = person['age'] ) )

#Формат
human = {
    'name': 'Laura',
    'age' : 55
    }
print('Імя: {person[name]}\nВік: {person[age]}'.format( person = human ) )


# ****Jessy**** ^
# Jessy******** <
# ********Jessy >
# ____Jessy____
# ASSDFJSSDKJSJ
# KJDJNCKSJNKf_
input_str = 'Jessy'
print( '{0:*^15}'.format( input_str))
print( '{0: ^15}'.format( input_str))
print( '{0:^15}'.format( input_str))
print( '{0:_^15}'.format( input_str))

#вирівнювання автоматично метод 1
input_str = 'Jessy'
length =14

if( len(input_str) % 2):
  length += 1


print( ('{0:*^'+str(length)+'}').format( input_str))


#вирівнювання автоматично метод 2
# input_str = 'Jessy'
# if (len(name) % 2) == 0:
#  print( '{0:*^12}'.format(name))
# else:
#  print( '{0:*^11}'.format(name))﻿

#
# one_more = 'Jessy'
# one_more = (length - len( input_str )) & 1
# print( ('{0:*^' + str(length + one_more)  + '}').format( input_str ) )﻿

#
# name = str(input("Your name?\n"))
# length = len(name)
# length += 6
# print('{0:_^{1}}'.format(name, length))﻿


#

# if len(input_str) % 2 == 0:
#   print('Hello {0:_^16}!'.format(input_str))
# else:
#   print('Hello {0:_^15}!'.format(input_str))﻿

#
input_str = 'Jessy'
length =11

if( len(input_str) % 2 == 0 and int(length) % 2 == 0):
  print( ('{0:/^'+str(length)+'}').format( input_str))
elif( len(input_str) % 2 == 0 and int(length) % 2 == 1):
  print( ('{0:+^'+str(1+length)+'}').format( input_str))
elif( len(input_str) % 2 == 1 and int(length) % 2 == 0):
  print( ('{0:=^'+str(1+length)+'}').format( input_str))
else:
  print( ('{0:$^'+str(length)+'}').format( input_str))

#
name = 'Juliav'
length = 11
#Условие
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0
length_2 = len(name) % 2 ==1 and int(length) % 2 == 1
length_3 = len(name) % 2 ==1 and int(length) % 2 == 0
# length_4 = len(name) % 2 ==0 and int(length) % 2 == 1

if length_1:
  print( ('{0:$^'+str(length)+'}').format( name))
elif length_2:
  print( ('{0:*^'+str(length)+'}').format( name))
elif length_3:
  print( ('{0:+^'+str(1+length)+'}').format( name))

else:
  print( ('{0:=^'+str(1+length)+'}').format( name))

#
name = 'Klara'
length = 14
#Условие name и length
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0
length_2 = len(name) % 2 ==1 and int(length) % 2 == 1
length_3 = len(name) % 2 ==1 and int(length) % 2 == 0
length_4 = len(name) % 2 ==0 and int(length) % 2 == 1

#Условие  print
Print1 = ('{0:$^'+str(length)+'}').format( name)
Print2 = ('{0:*^'+str(length)+'}').format( name)
Print3 = ('{0:+^'+str(1+length)+'}').format( name)
Print4 = ('{0:=^'+str(1+length)+'}').format( name)

if length_1:
  print( Print1 )
elif length_2:
  print( Print2 )
elif length_3:
  print( Print3 )
else:
  print( Print4 )


#
name = 'Razor'
length = 10
#Условие name и length
length_1 = len(name) % 2 ==0 and int(length) % 2 == 0 or len(name) % 2 ==1 and int(length) % 2 == 1
length_2 = len(name) % 2 ==1 and int(length) % 2 == 0 or len(name) % 2 ==0 and int(length) % 2 == 1

#Условие  print
Print1 = ('{0:@^'+str(length)+'}').format( name)
Print2 = ('{0:@^'+str(1+length)+'}').format( name)

if length_1:
  print( Print1 )
else:
  print( Print2 )
