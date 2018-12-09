a = set('helllo')
print(type(a))
print(a)

a = {'23' : 32}
print(type(a))
print(a)

a = {'23', 32}
print(type(a))
print(a)

a = {i ** 2 for i in range(10)}
print(type(a))
print(a)

a = {i ** 2 for i in range(10)}
a = {}
print(type(a))
print(a)

a = {i ** 2 for i in range(10)}
a = {23}
print(type(a))
print(a)

a = set('helllo')
b = frozenset('Qwerty')
a.add(1)
#b.add(1)   -error
print('a: ', a)

a = ['r', 's', 'w', 'a', 'a', 's']
print(a)
print('set(a): ', set(a))


a = {32, 45, 43.3, 76}
print('len(a): ', len(a))


a = {32, 45, 43.3, 76}
x = 33 
print('x in a :', x in a)


a = {32, 45, 76, 96}
x = {33, 46, 77} 
print('a.isdisjoint (x): ', a.isdisjoint (x))


a = {32, 45, 76, 96}
x = {32, 45, 76, 96} 
print('a == x : ', a == x)


a = {32, 45, 76, 96}
x = {33, 45, 77, 96} 
a.update(x)
print('a.update(x): ', a)


a = {32, 45, 76, 96}
x = {33, 45, 77, 96} 
a.intersection_update(x)
print('a.intersection_update(x): ', a)


a = {32, 45, 76, 96}
x = {33, 45, 77, 96} 
a.difference_update(x)
print('a.difference_update(x): ', a)


a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.symmetric_difference_update(x)
print('a.symmetric_difference_update(x): ', a)


a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.add (23)
print('a.add: ', a)

a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.remove (30)
print('a.remove: ', a)


a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.discard (1000)
print('a.discard: ', a)


a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.pop ()
print('a.pop: ', a)


a = {30, 45, 77, 96, 5}
x = {43, 45, 15, 1,  5} 
a.clear ()
print('a.clear: ', a)