n = input('vvedit cile chyslo: ')

while type(n) != int:
	try:
		n = int(n)
	except:
		print('Neprawylno vvely!')
		n = input('vvedit cile chyslo: ')

if n % 2 == 0:
	print('Parne')
else:
	print('Neparne')


total = 100

i = 0
while i < 5:
	n = int(input())
	total -= n
	i += 1


total = 100

while total > 0:
	n = int(input())
	total = total - n
if total == 0:
	print('resurs vycherpano')
else:
	print('nedopustyma operacija')


total = 100

while total > 0:
	n = int(input())
	if n <= total:
		total = total - n
	else:
		print('nemozlyvo vidhjaty', total, "vid", n)
		break
print('zaluchulos vidnjaty', total)



total = 100

while total > 0:
	n = int(input())
	if n > total:
		print('nemozlyvo vidhjaty', n, "zi", total)
		break
	total = total - n

print('zaluchulos vidnjaty', total)




i = 0
while i <= 20:
	print(i)
	print(2**i)
	i += 1


i = 0
while i <= 20:
	print(i)
	print("%.7d" % 2**i)
	i += 1


i = 0
while i <= 20:
	print(i)
	print("%7d" % 2**i)
	i += 1