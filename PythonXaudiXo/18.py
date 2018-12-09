# Срез списком [List slicing & indexing]

#idex
dig = [ 1,2,3,4,5,6,7,8,9,10]
dig1 = dig[4]
print(dig1)  #5


#List indexing
dig2 = [ 1,2,3,4,5,6,7,8,9,10]
dig3 = dig2[2:4 ]  #виведе po index  - [3,4]
#dig2 = dig[ :4 ]від початку і до 4 index.
#dig2 = dig[3: ]від 3 index до кінця.
#dig2 = dig[::2 ] index Шаг через 2 вивееде -1,3,5,7,9
#dig2 = dig[::3 ] index Шаг через 2 вивееде -1,4,7,10
print(di g3)  #[3, 4]


#pryklad range
dig4 = range(44, 85)[::10]  #виведе po index  - [3,4]
for i in dig4:
  print(i)
  # 44
  # 54
  # 64
  # 74
  # 84


#range -prykla
for i in range(1000, 1017)[::5]:
  print(i)
  # 1000
  # 1005
  # 1010
  # 1015


for i in range(80, 99, 8):
  print(i)
  # 80
  # 88
  # 96


#zadachka kortez
sqr = 0,1,4,9,16,25,36,49,64,81
print( sqr[1::4]) #(1, 25, 81)


# Negatyvni znachennja -отримаємо цифру 8
dig5 = [ 1,2,3,4,5,6,7,8,9,10]
dig6 = dig5[-2-1]  #це -2-1= -3 отримаємо цифру 8
                   #index -3 рахує з кінця
print(dig6) #8

#Срезка негативного значення:
dig7 = [ 1,2,3,4,5,6,7,8,9,10]
dig8 = dig7[-4:-1]

print(dig8)  #отримаємо цифри [7,8,9]

#revers
dig9= [ 1,2,3,4,5,6,7,8,9,10]
dig10 = dig9[::-1]
print(dig10) #отримаємо цифри [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

dig11= [ 1,2,3,4,5,6,7,8,9,10]
dig12 = dig11[::-1][::-1]
print(dig12) #отримаємо цифри [ 1,2,3,4,5,6,7,8,9,10]

# zadachka:
sg = 0,1,4,9,16,25,36,49,64,81
print(sg[7:5:-1])     #виведе[49,36]

sg = 0,1,4,9,16,25,36,49,64,81
print(sg[5:7:-1])  #()

sg = 0,1,4,9,16,25,36,49,64,81
print(sg[5:7]) #(25, 36)

dig2 = [ 1,2,3,4,5,6,7,8,9,10]
dig3 = dig2[2:8]  #виведе po index  - [3,4]
print(dig3) #[3, 4, 5, 6, 7, 8]

