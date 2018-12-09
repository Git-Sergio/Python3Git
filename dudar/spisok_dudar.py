l = []
lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
print (lis)

a = [a + b for a in 'listen' if a!= 's' for b in 'soup' if b != 'u']
print(a)

l.append(23)
l.insert(1, 56)
l.append(35)
l.append(35)
l.remove (35)
b = [24, 24, 67]
l.extend(b)
l.pop(0)
print('l.index 56:', l.index(56))
print('l.count 24:', l.count(24))
l.sort()
print('l.index 56:', l.index(56))
l.reverse()
print(l)
print(l)

l.clear()
print(l)

#
l = [34, 'sd', 56, 34.34]
print(l[-1])


#
i = 0
while i < 4:
	print('while i < 4:= l[i] =', l[i])
	i += 1

print('l=', l)
print('l[1:]=', l[1:])
print('l[:3]=', l[:3])
print('l[::-2]=', l[::-2])
print('l[-2::-2]=', l[-2::-2])