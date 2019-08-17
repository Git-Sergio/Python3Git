
try:
	old = int(input('Your Old: '))
except ValueError:
	print("ValueError-Vvedit cile chyslo")
	quit()

print('Recomendet', end=' ')

if 3 <= old < 6:
	print('"lion King"')
elif 6 <= old <12:
	print('"Ninjago"')
elif 12 <= old < 16:
	print('"Robocop"')
elif 16 <= old:
	print('"PoliRobocar:))"')
else:
	print("Vy zamalenki dlja filmiv")




try:
	num = int(input())

except ValueError:
	print("Vvedit cile chyslo - ValueError")
	quit()

print('num', end=' ')
if num < 0:
	print(-1)
elif num > 0:
	print(1)
else:
	print(0)
