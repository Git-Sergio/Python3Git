# Напишите программу, на вход которой подаётся список чисел одной строкой. 
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
#  находящий на противоположном конце этого списка. Например, если на вход 
#  подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" 
#  (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# Sample Input 1:

# 1 3 5 6 10
# Sample Output 1:

# 13 6 9 15 7
# Sample Input 2:

# 10
# Sample Output 2:

# 10


a=[int(i) for i in input().split()]
b=0
c=0
d=''
for i in range(len(a)-1):
    if len(a)!=1:
        b = a[i-1]+a[i+1]
        d=str(d)+str(b)+' '
if len(a)!=1 :
    d=d+str(a[-2]+a[0])    
if len(a)==1 :
    d=str(a[0])
print(d)



#
# a=[int(i) for i in input().split()]
# n=len(a)
# if n==1:
#     print(a[0])
# else:
#     print(a[1]+a[n-1],'',end='')
#     for i in range(1,n-1):
#         print(a[i-1]+a[i+1],'',end='')
#     print(a[0]+a[n-2])



#
# list=[int(i) for i in input().split()]
# if len(list)>1:
#  last=[list[-1]]
#  first=[list[0]]
#  list2=last+list+first
#  result=[]
#  j=1
#  for i in range(1,len(list2)-1):
#    s=int(list2[j-1])+int(list2[j+1])
#    result.append(s)
#    j+=1
#  print(*result)
# else:
#     print(*list)


#
# list = [int(j) for j in input().split()]
# s = 0
# x = len(list)
# if x > 2:
#   for i in list:
#     if s == (x - 1):
#       i = list[s - 1] + list[0]
#       print(i, end = ' ')
#     if s < (x - 1):
#       i = list[s - 1] + list[s + 1]
#       s = s + 1
#       print(i, end = ' ')
# if x < 2:
#   print(list[0])


#
# list = [int(x) for x in input().split()]
# if len(list) == 1:
#     print (list[0])
# else:
#     for i in range(0, len(list)):
#         if i == (len(list) - 1):
#             print(list[i - 1] + list[0])
#         else:
#             print(list[i - 1] + list[i + 1], end=' ')


#
# a=[int(i) for i in input().split()]
# f,g=-(len(a)),-1
# for i in range(0,len(a)):
#     f+=1
#     if len(a)==1:
#         print(a[0])
#         break
#     else:
#         print(a[f]+a[g],end=' ')
#     g+=1



#
# a = [int(i) for i in input().split()]
# for i in range(len(a)-1):
#     print(a[i-1] + a[i+1], end=' ')
# print(a[0] + sum(a[-2:-1]))


#
# a = [int(i) for i in input().split()]
# i = 0
# s = 0
# if len(a) == 1:
#     print(*a)
# else:
#     a.append(a[0])
#     a.insert(0, a[-2])
# for i in range(1, len(a)-1):
#         s = (a[i-1] + a[i+1])
#         i += 1
#         print(s)



#
# l = [int(i) for i in input().split()]
# print(*[sum(i) for i in zip(l[-1:]+l[:-1], l[1:]+l[0:1])], sep=' ') if len(l)>1 else print(l[0])




#         
# a = [int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)], end=' ')
# else:
#     print(a[0])



#
# exec('''
# def sdf(a):
#     b = []
#     if len(a) == 1:
#         return a
#     for i in range(len(a)):
#         if i == len(a) - 1:
#             b.append(int(a[i - 1]) + int(a[0]))
#         else:
#             b.append(int(a[i - 1]) + int(a[i + 1]))
#     return b
# for j in sdf([int(i) for i in input().split()]):
#     print(j, end=" ")
# ''')



#
# a = [int(j) for j in input().split()]
# if len(a) != 1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i-(len(a)-1)], end = ' ')
# else:
#     print(a[0])