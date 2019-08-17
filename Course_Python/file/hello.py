

# l = [str(i)+str(i-1) for i in range(20)]
# l = [line.strip() for line in f]
f = open("test1.txt", 'r')
l = [line.strip() for line in f]
print(l)
z = [str(l)]
x = open('test2.txt', 'w')
for y in z:
    x.write(y)

# for index in l:
#     f.write(index + '\n')
#
# print(f)
#
# x = open('test2.txt', 'w')
# for z in str(f):
#     x.write(z)
# f.write("This is a test!")

f.close()
x.close()