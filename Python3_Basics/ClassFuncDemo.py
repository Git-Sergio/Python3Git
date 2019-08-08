class MyClass:
    name = 'Sergio'

    def sum(selfself, a,b):
        print (a+b)

x = MyClass()
print (x.name)         #Sergio
print (x.name)
x.sum(4,5)             #9



class MyClass:
    name = 'Sergio'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(selfself, a,b):
        print (a+b)

x = MyClass('John', 40)
print (x.name)         #Sergio
x.sum(4,5)             #9
#del x.name
#print (x.name)         #Sergio
print (x.age)         #Sergio
