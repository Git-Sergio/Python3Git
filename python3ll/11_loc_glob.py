# def rectangle():
#     a = float(input("Ширина:"))
#     b = float(input("Высота :"))
#     print("Площадь: %.2f" % (a*b))
 
# def triangle():
#     a = float(input("Основание %s: " % figure))
#     h = float(input("Высота %s: " % figure))
#     print("Площадь: %.2f" % (0.5 * a * h))
 
# figure = input("1-прямоугольник, 2-треугольник: ")
# if figure == '1':
# 	rectangle()
# elif figure == '2':
# 	triangle()




result = 0
 
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a*b
 
def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    result = 0.5 * a * h
 
figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
	rectangle()
elif figure == '2':
	triangle()
 
print("Площадь: %.2f" % result)



#

s_circle = 0

def cylinder():
	def circle():
		global s_circle
		s_circle = 3.14 * r**2
	r = float(input())
	h = float(input())
	s_cylinder = 2 * 3.14 * r * h
	if input("Bokova - 1, Povna - 2: ") == '2':
		circle()
		s_cylinder += 2 * s_circle
	print(s_cylinder)

cylinder()