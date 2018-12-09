# apples = 100
# eat_day = 5
# day = 7
# apples = apples - eat_day * day
# print(apples)

var_int = 10
print(var_int)

var_float = 8.4
print(var_float)

var_str = "NO"
print(var_str)

big_int = var_int *3.5
print(big_int)

var_float = var_float - 1
print(var_float)

x= (var_int / var_float) 
print(x)

y= big_int / var_float
print(y)

print(var_int)
print(var_float)

var_str = var_str * 2 + "Yes" * 3 #"NoNoYesYesYes"
print(var_str)

print(big_int)

print("a: ", 1)

one = 1
two = 2
print( one, two)

print("hello" + " " + "world" )
print(10 - 2.5/2)

# print("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", sep="-")
# print(1, 2, 3, sep="//")
# print(10, end="")
# print(10, end="\n")
# print(10, end="\n\n")

pupil = "Ben"
old = 16
grade = 9.2
print ("It's %s, %d. Level: %.15f" % (pupil, old, grade))

# %d - int
# %.12f - float
# %s - str

print("This is a {0}. I'ts {1}.")

print ("This is a {0}. I'ts {1}.".format("ball", "red"))

print("This is a {0}. I'ts {1}.".format("cat", "white"))

print("This is a {0}. I'ts {1} {2}.".format(1, "a", "number"))


# nameUser = input("Your name: ")
# cityUser = input("Your City: ")
# print("Your name {0}. Your City {1}.".format(nameUser, cityUser))

kgOranges = int(input("kg Orange: "))
priceOrange = float(input("Price: "))
sumOrange = kgOranges * priceOrange
print("Summ: ", sumOrange, "usd")