# Жители страны Малевии часто экспериментируют с планировкой комнат. 
# Комнаты бывают треугольные, прямоугольные и круглые. 
# Чтобы быстро вычислять жилплощадь, требуется написать программу,
#  на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
#   которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
# Формат ввода, который используют Малевийцы:
# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника
# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника
# круг
# r
# где r — радиус окружности

# Sample Input 1:
# прямоугольник
# 4
# 10
# Sample Output 1:
# 40.0
# Sample Input 2:
# круг
# 5
# Sample Output 2:
# 78.5
# Sample Input 3:
# треугольник
# 3
# 4
# 5
# Sample Output 3:
# 6.0

figure = str(input())

if figure == 'треугольник':
	a = float(input())
	b = float(input())
	c = float(input())
	p = (a + b + c) / 2
	S = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
	print (S)

elif figure == 'прямоугольник':
	a = float(input())
	b = float(input())
	S = a*b
	print(S)

elif figure == 'круг':
	r = float(input())
	Pi = 3.14
	S = Pi * (r ** 2)
	print(S)



#
# x=input()
# if x=='треугольник':
#   a=int(input())
#   b=int(input())
#   c=int(input())
#   p=(a+b+c)/2
#   s=float((p*(p-a)*(p-b)*(p-c))**0.5)
#   print(s)
# elif x=='прямоугольник':
#   a=int(input())
#   b=int(input())
#   S=float(a*b)
#   print(S)
# elif x=='круг':
#   r=int(input())
#   s=float(3.14*r**2)
#   print(s)


#
# figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
#           'прямоугольник': [2, lambda a, b: a*b], 
#           'круг': [1, lambda r: 3.14*r**2]}
# f = input()
# print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))




#
# res = r'''
# figure = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
#           'прямоугольник': [2, lambda a, b: a*b], 
#           'круг': [1, lambda r: 3.14*r**2]}
# f = input()
# print(figure[f][1](*(float(input()) for _ in range(figure[f][0]))))
# '''
# exec(res)




#
#MastHawe!!!
# exec('''
# def s1(a, b, c):
#   p = (a + b + c) / 2
#   return float( ( p * (p - a) * (p - b) * (p - c) ) ** (1 / 2) )

# figure = {'треугольник': [3, lambda a, b, c: s1(a, b, c)], 
#           'прямоугольник': [2, lambda a, b: a * b], 
#           'круг': [1, lambda r: 3.14 * r**2 ]}
# f = str(input())
# print(figure[f][1](*(float(input()) for _ in range(figure[f][0]))))
# ''')