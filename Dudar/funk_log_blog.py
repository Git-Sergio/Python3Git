def height(m, cm):
	total = (m * 100) + cm
	print(str(total) + ' cm tall')
height(1,70)


def calc(a, b):
	total = a + b
	return total

summ = calc(4,5)
print(summ)



arr = [1,12,12,12,10,214,455]
sum = 0
for i in arr:
	if i >= 100 or i <=11:
		# break
		continue
	sum += i 
print(sum)


