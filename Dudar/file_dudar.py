# f = open('file.txt')
# print(f.read(5))


f = open('file.txt')
for line in f:
	print(line)


f = open('file.txt', 'a')
f.write ('Hello, it\'s me! \n')
f.close()

f = open('file.txt')
for line in f:
	print(line)