#Hello
def hello(x):
    if x == 0:
        return
    else:
        print('Hello World!')
        hello(x-1)

hello(4)

# Summ
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))    #24


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(6))    #720


#Fibonacci
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


print(fibo(7))      #13