def dec(func):
	def wraper():
		print('Kod do vykonannja funkcii dec 1')
		func()
		print('Kod jakyj spracuvav pislja funkcii  dec 1')
	return wraper

def test(func):
	def wraper():
		print('Kod do vykonannja funkcii test 2')
		func()
		print('Kod jakyj spracuvav pislja funkcii test 2')
	return wraper


@dec
@test
def show():
	print('Ja zvychajna funkcia 0')

# show = decorator(show)
show()

