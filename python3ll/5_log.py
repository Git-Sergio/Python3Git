x = 5
y = 13

a = x == y and x <= y
print (a) #False

b = x != y and x <= y
print (b) #True


c = x >= y or x == y
print (c) #False

d = x > y or x < y
print (d) #True

e = 'sergio' > 'sergi'
print (e) #True

s1 = 'hello' #chyslovyj nomer menshe
s2 = 'world' #chyslovyj nomer bilshe
x = s1 > s2
print (x) #False
x = s1 and s2
print (x) #world
x = s1 or s2
print (x) #hello

ch1 = int(input("chuslo pershe: "))
ch2 = int(input("chuslo druge: "))
print ('Pershe chyslo bilshe za druge: ', (ch1 > ch2) )