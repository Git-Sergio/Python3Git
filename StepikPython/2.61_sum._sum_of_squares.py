# Напишите программу, которая считывает с консоли числа (по одному в строке) 
# до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого 
# выводит сумму квадратов всех считанных чисел.

# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
 # после этого считывание продолжать не нужно.

# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем,
 # что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая 
 # внимания на то, что остались ещё не прочитанные значения.﻿

# Sample Input:

# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# Sample Output:

# 340


i=0
k=0
while True:
    x=int(input())
    i=i+x
    k=k+x**2
    if i==0:
        break
print(k)




#

# s, j = 0, 0
# while True:
#     a = int(input())
#     s += a
#     j += a**2
#     if s == 0:
#         print(j)
#         break
# На будущее - объявление переменных в строку ускоряет обработку. 
# Без онного результат получился бы 7.87.

#

# s = [int(input())]
# x = 0
# k = 0
# while s != 0:
#     if i == 0  :
#         print(x)
#     s = x + s
#     i = s
#     k = s ** s
#     s = int(input())
# print(x)




#
# a = [int(input())]
# x = 0
# for i in a:
#     if sum(a) != 0:
#         a.append(int(input()))
#     else:
#         for q in a:
#             q *= q
#             x += q
# print(x)





#
# summa=0
# summa_sq=0
# while True:
#     inp=int(input())
#     summa=summa+inp
#     summa_sq=summa_sq+inp**2
#     if summa==0:
#         break
# print(summa_sq)



#
# s = 0
# p = 0
# while True:
#     i = int(input())
#     p += i * i
#     s = s + i
#     if s == 0:
#         break
# print(p)




#
# s2 = 0
# s = '0'
# while s != 0:
#     s = int(s)
#     a = int(input())
#     s += a
#     s2 += (a*a)
# print(s2)  