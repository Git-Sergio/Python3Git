
a = input()
b = input()
try:
	x = float(a)
	y = float(b)
	c = x + y
	print(c)
	print(int(c))
except ValueError:
	a = str(a)
	b = str(b)
	c = a + b
	print(c)

# a = input()
# b = input()
# try:
# 	x = float(a)
# 	y = float(b)
# 	print(a+b)
# except ValueError:
# 	print(x+y)

