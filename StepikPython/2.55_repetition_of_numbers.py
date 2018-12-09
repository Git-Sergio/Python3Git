# Напишите программу, которая принимает на вход список чисел в одной строке
#  и выводит на экран в одну строку значения, которые повторяются в нём более 
#  одного раза.

# Для решения задачи может пригодиться метод sort списка.

# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3
# Sample Input 4:
# 1 1 1 1 1 2 2 2
# Sample Output 4:
# 1 2




a = [int(i) for i in input().split()]
b = [] 
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
print(*(b))



#
# a = input().split()
# print(' '.join(n for n in set(a) if a.count(n)>1))



# 
# a = sorted([int(n) for n in input().split(' ')])
# for i in set(a):
#     b = a.count(i)
#     if b>1 :
#         print(i, end=' ')


#
# a=[int(i) for i in input().split()]
# a.sort()
# count = 0

# if a.__len__() < 2:
#     pass
# else:
#     for i in range(len(a)):

#         x = a[i]
#         y = a[i + 1 - a.__len__()]
#         if x == y:
#             count = 1
#         elif x != y and count > 0:
#            print(x, end=" ")
#            count = 0

#     if count > 0:
#         print(x)




#
# a = [int(i) for i in input().split()]
# a.sort()
# i = 0
# for j in range(0, len(a)):
#     if i == len(a):
#         break
#     if a.count(a[i]) >= 2:
#         print(a[i], end=' ')
#         i += a.count(a[i])
#     else:
#         i += 1


#
# spisok = input().split()
# for x in set(spisok):
#     spisok.remove(x)
# print(*set(spisok))



# #
# spisok = input().split()
# for x in set(spisok):
#     spisok.remove(x)
# print(" ".join(list(set(spisok))))



#
# a = [int(i) for i in input().split()]
# b = []

# for i in a:
#     if a.count(i) > 1 and i not in b:
#         b.append(i)

# for i in b:
#     print(i, end=" ")


#
# a = [int(i) for i in input().split()]
# b = []
# for j in range(len(a)):
#     if a.count(a[j]) >= 2 and a[j] not in b:
#                 b.append(a[j])
# print(*b)


#
# s= [int(i) for i in input().split()]
# s.sort()
# y=len(s)
# for i in s[:]:
#     if y==0:
#         break
#     i=s[0]
#     x=s.count(i)
#     if y==1:
#         break
#     if s[0]==s[1]:
#         print (s[1],end=' ')
#     del s[0:x]
#     y=len(s)



#
# n,s = [int(s) for s in input().split()], []
# for i in n:
#     if n.count(i)>1:
#         s+=[i]
# print(*set(s))


#
# l = input().split()
# s = set()
# for x in l:
#     if l.count(x) > 1:
#         s.add(x)
# print(*s)


#
# s = input().split()
# s.sort()
# p = ''
# s1 = list(set(s))
# for i in range(len(s1)):
#     if s.count(s1[i])>1:
#         p+=str(s1[i])+' '
# print(p)


#
# l = input().split()
# print(*{x for x in l if l.count(x) - 1})