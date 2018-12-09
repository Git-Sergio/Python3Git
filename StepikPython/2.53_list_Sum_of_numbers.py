# Напишите программу, на вход которой подается одна строка с целыми числами 
#(пробіл між числами).
#  Программа должна вывести сумму этих чисел.

# Используйте метод split строки. ﻿﻿

# Sample Input:

# 4 -1 9 3
# Sample Output:

# 15



a = input().split()
s = 0
for i in a:
    s+=int(i)
print(s)



#
# a = [int(i) for i in input().split()]
# print(sum(a))

#
# s = 0
# for i in (int(i) for i in input().split()):
# 	s+=i
# print(s)


#
# b = 0
# a = input().split()
# for i in range(len(a)):
#     b = b + int(a[i])
# print(b)



#
# print(sum([int(x) for x in input().split()]))


#
# a = [int(x) for x in input().split()]
# s=0
# for i in a:
#     s=s+i
# print(s)


#
# a=[int(i) for i in input().split()]
# b=0
# for i in range(len(a)):b=b+a[i]
# print(b)



# a = [int(i) for i in input().split()]
# x = sum(a)
# print(x)