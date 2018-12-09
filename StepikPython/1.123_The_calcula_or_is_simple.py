# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым 
# числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
# mod — это взятие остатка от деления, 
# pow — возведение в степень, 
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку 
# "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:

# 5.0
# 0.0
# mod
# Sample Output 1:

# Деление на 0!
# Sample Input 2:

# -12.0
# -8.0
# *
# Sample Output 2:

# 96.0
# Sample Input 3:

# 5.0
# 10.0
# /
# Sample Output 3:

# 0.5



a = float(input())
b = float(input())
c = str(input())

if c == '+':
	print (a + b)

elif c == '-':
	print (a - b)

elif c == '/':
	if b != 0:
		print (float(a) / float(b))
	else:
		print("Деление на 0!")

elif c == '*':
	print (a * b)

elif c == 'mod':              #mod — это взятие остатка от деления, 
	if b != 0:
		print (float(a) % float(b))
	else:
		print("Деление на 0!")

elif c == 'pow':              #pow — возведение в степень, 
	print (float(a) ** float(b))

elif c == 'div':              #div — целочисленное деление.
	if b != 0:
		print (float(a) // float(b))
	else:
		print("Деление на 0!")






#
# first = float(input())
# second = float(input())
# action = input()
# operations = {"mod": "%", "div": "//", "pow": "**"}
# try:
#     print(eval("(" + str(first) + ")" + operations.get(action, action) + str(second)))
# except ZeroDivisionError:
#     print('Деление на 0!')



#
# a = float(input())
# b = float(input())
# act = input()

# if (act=="/" or act=="mod" or act=="div") and b==0:
#     c = "Деление на 0!"
# elif act=="+":    c = a + b
# elif act=="-":    c = a - b
# elif act=="/":    c = a / b
# elif act=="*":    c = a * b
# elif act=="mod":  c = a % b
# elif act=="pow":  c = a ** b
# elif act=="div":  c = a // b

# print (c)


#
# a = float(input())
# b = float(input())
# op = input()
# if(b == 0 and (op == "mod" or op == "/" or op == "div")):
#     print("Деление на 0!")
# elif(op == '+'):
#     print(a + b)
# elif(op == '-'):
#     print(a - b)
# elif(op == '*'):
#     print(a * b)
# elif(op == '/'):
#     print(a / b)
# elif(op == 'mod'):
#     print(a % b)
# elif(op == 'pow'):
#     print(a ** b)
# elif(op == 'div'):
#     print(a // b)
# else: print("Unknown operator")


#
# import operator
# operators = {'+':operator.add, '-':operator.sub, '/':operator.truediv,'*':operator.mul, 'mod':operator.mod, 'pow':operator.pow, 'div':operator.floordiv}
# a = float(input())
# b = float(input())
# op = input()
# try:
#     print(operators[op](a, b))
# except ZeroDivisionError:
#     print('Деление на 0!') 



#
# import operator

# operations = {
#   '+': operator.add,
#   '-': operator.sub,
#   '/': operator.truediv,
#   '*': operator.mul,
#   'div': operator.floordiv,
#   'mod': operator.mod,
#   'pow': operator.pow,
# }

# x, y, op = float(input()), float(input()), str(input())

# if op in ['/', 'mod', 'div'] and y == 0.0:
#   print("Деление на 0!")
# else:
#   print(operations[op](x, y)


#
# a, b, c = '('+input()+')', input(), input()
# d = {'+':'+', '-':'-', '/':'/', '*':'*', 'mod':'%', 'pow':'**', 'div':'//'}
# print ('Деление на 0!' if c in 'div/mod' and float(b)==0 else eval(a+d[c]+b))



#
# exec("exec (\"print(str(a+b)*(op == '+')+ str(a*b)*(op == '*') + str(a-b) * (op == '-') + 'Деление на 0!' * (((op == '/') or(op == 'mod') or (op == 'div')) and b==0)  + str(str(a/b) if (b != 0 and op == '/') else '') + str(str(a % b) if (b != 0 and op=='mod') else '') + str(str(a // b) if (b != 0 and op=='div') else '') + str((a)** b) * (op == 'pow'))\", {'a':float(input()), 'b':float(input()), 'op':input() })")




#
# x=float(input())
# y=float(input())
# z=input()
# if (z=='/' and y==0.0) or (z=='mod' and y==0.0) or (z=='div' and y==0.0):
#     print('Деление на 0!')
# elif z=='+':
#     print(x+y)
# elif z=='-':
#     print(x-y)
# elif z=='/':
#     print(x/y)
# elif z=='*':
#     print(x*y)
# elif z=='mod':
#     print(x%y)
# elif z=='pow':
#     print(x**y)
# elif z=='div':
#     print(x//y)