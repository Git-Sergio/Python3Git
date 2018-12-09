# def cylinder():
#     r = float(input())
#     h = float(input())
#     # площадь боковой поверхности цилиндра:
#     side = 2 * 3.14 * r * h
#     # площадь одного основания цилиндра:
#     circle = 3.14 * r**2
#     # полная площадь цилиндра:
#     full = side + 2 * circle
#     return full
 
# square = cylinder()
# print(square)
# # print(cylinder())



def cylinder():
    try:
        r = float(input())
        h = float(input())
    except ValueError:
        return
    side = 2 * 3.14 * r * h
    circle = 3.14 * r**2
    full = side + 2 * circle
    return full,circle,side

print(cylinder())


# def cylinder():
#     r = float(input())
#     h = float(input())
#     side = 2 * 3.14 * r * h
#     circle = 3.14 * r**2
#     full = side + 2 * circle
#     return side, full
 
# sCyl, fCyl = cylinder()
# print("Площадь боковой поверхности %.2f" % sCyl)
# print("Полная площадь %.2f" % fCyl)
# print(cylinder())