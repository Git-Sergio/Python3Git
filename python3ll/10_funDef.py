
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a*b))
 
def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print("Площадь: %.2f" % (0.5 * a * h))
 
def circle():
    r = float(input("Радиус: "))
    print("Площадь: %.2f" % (3.14 * r**2))
 
figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
if figure == '1':
	rectangle()
elif figure == '2':
	triangle()
elif figure == '3':
	circle()
else:
	print("Ошибка ввода")


# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
 
# if figure == '1':
# 	a = float(input("Ширина: "))
# 	b = float(input("Высота: "))
# 	print("Площадь: %.2f" % (a*b))
# elif figure == '2':
# 	a = float(input("Основание: "))
# 	h = float(input("Высота: "))
# 	print("Площадь: %.2f" % (0.5 * a * h))
# elif figure == '3':
# 	r = float(input("Радиус: "))
# 	print("Площадь: %.2f" % (3.14 * r**2))
# else:
# 	print("Ошибка ввода")



def countFood():
	a = int(input())
	b = int(input())
	print("Vsiogo", a+b, "szt.")

print("skilky bananiv dlja mavp?")
countFood()
print("skilky jabluk dlja 1kg?")
countFood()
print("skilky kivi dlja pyroga?")
countFood()


# print("Сколько бананов и ананасов для обезьян?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
 
# print("Сколько жуков и червей для ежей?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
 
# print("Сколько рыб и моллюсков для выдр?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")


def positive():
    print("Pozytyvne chyslo")

def negatve():
    print("Negatyvne czyslo")

def test():
    a = int(input())
    if a > 0:
        positive()
    elif a < 0:
        negatve()
    else:
        print('Vy vvely "0"')
test()