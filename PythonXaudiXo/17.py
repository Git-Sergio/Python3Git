# Commenting   - #odnoctrocnyj   ''' mnogostrocnuy  '''
#pass   -дає змогу створювати пусті функції ,умови.
# Tuple   -Кортеж


                     #spysok
names = ['John', 'James', 'Jack']

names[0] = 'Michael'

print( names[0])  # ['Michael']
print( names )    # ['Michael', 'James', 'Jack']


#Tuple -Кортеж не можна міняти як попередній приклад
digits = (1,2,3,4,5)  #digits і digits1  одно і то саме
digits1 = 1,2,3,4,5   #digits і digits1  одно і то саме
names = ('John', 'James', 'Jack')
names1 = 'John1', 'James2', 'Jack3'

# names[0] = 'Michael'   видасть помилку

print( names[0])  # John
print( names )    # ('John', 'James', 'Jack')
print( names1 )   # ('John1', 'James2', 'Jack3')


#zadachka -що виведе
tuple = (1,(2,3,4,(5,6,7,8)))
print(((tuple[1])[3])[2])
