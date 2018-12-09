# Напишите программу, которая получает на вход три целых числа, 
# по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
#  потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a = int(input())
b = int(input())
c = int(input())

if (a >= c >= b):
	print(a)
	print(b)
	print(c)

elif (a >= b >= c):
	print(a)
	print(c)
	print(b)

elif (b >= c >= a) :
	print(b)
	print(a)
	print(c)

elif (b >= a >= c) :
	print(b)
	print(c)
	print(a)

elif (c >= a >= b) :
	print(c)
	print(b)
	print(a)

elif (c >= b >= a) :
	print(c)
	print(a)
	print(b)


#
# a,b,c = int(input()), int(input()), int(input())

# if a < b:
# 	a, b = b, a
# if a < c:
# 	a, c = c, a
# if b > c:
# 	b, c = c, b
# print(a)
# print(b)
# print(c)


#
# x=sorted([int(input()),int(input()),int(input())])
# print (x[2], x[0], x[1], sep="\n")


#
# a,b,c=int(input ()),int(input ()),int(input ())
# if a<b: a,b=b,a
# if a<c: a,c=c,a
# if b<c: c,b=b,c
# print (a,c,b,sep='\n')


#
# x = [int(input()) for i in range(3)]
# print(max(x),"\n", min(x),"\n", sum(x) - max(x) - min(x))



#
# x = int(input())
# y = int(input())
# z = int(input())
# a = min(x, y, z)
# b = max(x, y, z)
# c = x + y + z - a - b
# print(b)
# print(a)
# print(c)



#
# a,b,c=(int(input()) for i in range (3))
# print(str(max(a,b,c))+'\n'+str(min(a,b,c))+'\n'+str((a+b+c)-(max(a,b,c))-(min(a,b,c))))




#
# Lst = [int(input()), int(input()),int(input())]
# Lst.sort()
# print(Lst[2])
# print(Lst[0])
# print(Lst[1])


#
# a, b, c = [int(input()) for i in range(3)]
# print(max(a, b, c))
# print(min(a, b, c))
# print((a + b + c) - (max(a, b, c) + min(a, b, c)))


#
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a, b, c), min(a, b, c), sum((a, b, c)) - (max(a, b, c) + min(a, b, c)), sep='\n')


#
# lst = sorted([int(input()) for _ in range(3)])
# print (lst[2], lst[0], lst[1], sep="\n")



#
# num=[int(input()),int(input()),int(input())]
# num.sort()
# print(num[2])
# print(num[0])
# print(num[1])



#
# x=sorted([int(input()) for i in range(3)])
# print(x[2],x[0],x[1],sep='\n')