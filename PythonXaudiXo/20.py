# Функції для роботи з строками і числами

#join, replace, startswith, endswith, lower, upper, split
#min, max, abs, sum

#min
print( min([5,6,5,12,3,5,7,9,5,1852])) #min функція знайде і виведе мінімальне число
#max
print( max([5,6,5,12,3,5,7,9,5,1852])) #max функція знайде і виведе ммаксимальне число
#abs
print( abs(-325)) #abs функція  виведе абсолютне число 325
#sum
print( sum([2,10,15])) #sum функція  сумує всі числа в виведе суму 27


#.join
fruits = ['limon', 'apple', 'kivi', 'ananas', 'klubnika']
members = 'James,Joni,Jessi,Jak,John'

print( ' - '.join( fruits ) )  #.join (проставляє між словами те що ми напишемо в ' ')


#.split
fruits = ['limon', 'apple', 'kivi', 'ananas', 'klubnika']
members = 'James,Joni,Jessi,Jak,John'

print( members.split( ',' ) )  #.split(розділяє-по признаку який впишемо в ' ' і виводить масив)


#.replace
print( 'Hello, Petr!'.replace( 'Petr', 'Sergio' ) )  #.replace  (заміняє значення 1 на 2 replace('1', '2') -регістрочутливий)

# startswith
name = input('startswith Your Name: ')

if( name.startswith('S') ):
  print('Вітаємо вас! Проходіть!\nВи в елітном клубі людей, імя яких починається на букву "S"!')
else:
  print( 'Вітаємо вас!' )  # startswith (фільтрує по першій букві-регістрочутливий)

  # lower+startswith
name = input('startswith + lower Your Name: ')

if( name.lower().startswith('s') or name.lower().startswith('m')):
  print('Вітаємо вас! Проходіть!\nВи в елітном клубі людей, імя яких починається на букву "s" or "m"!')
else:
  print( 'Вітаємо вас!' )  # lower+startswith -(lower-переводить букви в маленький регістр ,потім startswith фільтрує по першій літері)

# endswith
word = 'Hello Swiming'

if( word.endswith('ing')):
  print('endswith- Hello ING!')
else:
  print( 'Hello!' )  # endswith -(фільтрує по останіх буквах-регістрочутливий)

#upper
input_str = input('введіть що небуть маленькими літерами: ')
print( input_str.upper() )   #upper (переводить в великий регістр)


#lower
input_str = input('введіть що небуть великими літерами: ')
print( input_str.lower() )   #lower(переводить в маленький регістр)
