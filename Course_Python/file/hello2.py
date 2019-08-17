f = open("test1.txt", 'r')
l = [line.strip() for line in f]
print(l)
z = [str(l)]
x = open('test2.txt', 'w')
for y in z:
    x.write(y)

f.close()
x.close()