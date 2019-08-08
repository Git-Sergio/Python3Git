
my_tuple = ('Apples', 'Oranges', 'Grapes')
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

# my_tuple[3] = 'Cherry'
# del my_tuple[2]

print(len(my_tuple))

my_tuple_2 = ('Banana',(1,2,3),['Tokio', 'Wroclaw'])
print(my_tuple_2)
print(my_tuple_2[2][1])

my_tuple_2[2][1] = 'Krakow'
print(my_tuple_2)

print('Banana' in my_tuple_2)     # True
print('Cherri' in my_tuple_2)      # False