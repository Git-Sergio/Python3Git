
# def name():
# 	a = input()
# 	b = input()
# 	c = a + b
# 	return c
# print(name())



# def name():
# 	a = input()
# 	b = input()
# 	c = a + b
# 	return c
# name()



# def name():
# 	a = input()
# 	b = input()
# 	return a + b
# print(name())


def height(m, cm):
	total = (m * 100) + cm
	print(str(total) + ' cm tall')
height(1,70)

def name():
	return input() + input()
print(name())


#
def height(m, cm):
	total = (m * 100) + cm
	print(str(total) + ' cm tall')
height(1,70)



#
def nul():
	nul = 1
	n = int(input())
	if n == 0:
		nul = 0
	while n != 0:
		nul *= n
		n = int(input())
	return nul
print(nul())
