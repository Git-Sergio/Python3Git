def f(x):
    return x**2

def perimetr(a,b,c):
    return a+b+c

def f(x):
    if x>0:
        return 'positive'
    else:
        return 'negative'

def f(x):
    return  x%10
a= [78,56,23,8,54512,65,95,2354,41,5000]
a.sort(key=f)

b = [78,56,23,8,54512,65,95,2354,41,5000]
b.sort(key=lambda x: x%10)



t = lambda x: 'positive' if x>0 else 'negative'
h = lambda : 'hello'
per = lambda a,b,c: a+b+c
r = lambda x: x**2

# print(t(0))