import math,time, os
import time
import os
import random as r
try:
	import noModule
except ImportError:
	print('Takogo Modula: noModule Nemaje')

import modul_dudar as m

from modul_dudar import hi
from modul_dudar import (hi, add)
from modul_dudar import (hi, add as a)

print(math.e)
print(math.pi)
print(math.cos(2))
print(math.tan(2))

print(time.time())

print(os.getcwd())
print(os.uname())

print(r.random())

print(m.add(45, 15))


hi()
print(add(45, 15))
print(a(45, 15))