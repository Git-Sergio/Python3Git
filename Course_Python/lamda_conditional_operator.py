f = lambda x: 'like' if x > 100 else 'Subscribe'
d = lambda x: 'like' if x > 100 else ('Subscribe' if x>0 else 'Follow me')
print(f(200))
print(d(-50))