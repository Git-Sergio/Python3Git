# Напишите программу, которая считывает со стандартного ввода целые числа, 
# по одному числу в строке, и после первого введенного нуля выводит сумму 
# полученных на вход чисел.

# Sample Input 1:

# 5
# -3
# 8
# 4
# 0
# Sample Output 1:

# 14
# Sample Input 2:

# 0
# Sample Output 2:

# 0


s = int(input())
i = 0
while s <= 0 or s >= 0:
    if s == 0  :
        print(i)
        break
    s = i + s
    i = s
    s = int(input())


#
# s, n =0, int(input())
# while n:
#     s, n = s + n, int(input())
# print(s)


#
# a = int(input())
# s = 0
# while a != 0 :
#     s += a
#     a = int(input())
# print(s)


#
# a,b = 1,0
# while a != 0:
#     a = int(input())
#     b += a
# print(b)



#
# a = 0
# b = None
# while b != 0:
#     b=int(input())
#     a = a + b
# print(a)



#
# x = 0
# a = 1
# while a != 0:
#         a = int(input())
#         x += a
# print(x)


#
# a = int(input())
# s = a
# while a != 0:
#   a = int(input())
#   s += a
# print(s)


#@
# import sys
# print(sum(int(x) for x in sys.stdin.readlines()))


#
# summa = 0
# i = True
# while i:
#     i = int(input())
#     summa += i
# print(summa)



#
# i = int(input())
# a = 0
# while i != 0:
#     a += i
#     i = int(input())
# print(a)


#
# s1, x = 0, 1
# while x:
#     x = int(input())
#     s1 += x
# print(s1)