def func(x, a):
	return x + a
print(func(23, 12))


def func(x, a):
	return x + a
print(func('Hello', 'World!'))


def func(x, a):
	res = x + a
	return res
print(func(20, 30))




def func(x):
	def add (a):
		return x + a
	return add

test = func (100)
print(test(200))



def func ():
	pass
print(func())


def func (r, w, y = 2):
	res = r + w
	res *= y
	return res
print(func(2, 4))


def func (r, w, y = 2):
	res = r + w
	res *= y
	return res
print(func(2, 4, 5))



def func (*args):
	return args
print(func('sd', 2, 4, 5.6))



def func (**args):
	return args
print(func(a=23, n=2, b=4, o=5.6))


def func (**args):
	return args
print(func(short='dict', longer='dictionary'))

