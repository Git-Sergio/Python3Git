try:
	x= int(input())
except ValueError:
	x = 0
	print("Vy Vvely ne chyslo")
	

try:
	y= int(input())
except ValueError:
	y = 0
	print("Vy Vvelychyslo")

else:
	print('vse OK')
	
finally:
	print('Vyvede 100% povidomlennja')

try:
	res = x / y
except ZeroDivisionError:
	print("Vy Vvely 0")
	res = 0
print(res)