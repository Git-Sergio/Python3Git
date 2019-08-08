#def func_name(parameter):
#    body

def printHello():
    print('Hello')
printHello()       #Hello


def printHi(name='John'):
    print('Hi, '+name)
printHi()          #Hi, John
printHi("Sergio")  #Hi, Sergio


def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)      #60


def returnSum(a,b):
    return (a+b)
x = returnSum(10,20)
print(x)            #30