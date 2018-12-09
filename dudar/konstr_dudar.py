class Person:
	name = 'Ivan'
	age = 10

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def set(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	course = 1
	scull = 152

	def set(self, name, age, course):
		self.name = name
		self.age = age
		self.course = course

igor = Student('Vasja', 19)
# igor._Person__set('Igor', 19)
print(igor.name)
print(igor.course)
igor.course = 2
print(igor.course)
print(igor.name)
print(igor.scull)
igor.set('Igor',23 , 5)
print('imja: ', igor.name, ', rist - ', igor.age, ', kurs - ', igor.course)



vlad = Person("Vlad", 25)
# vlad._Person__set("Vlad", 25)
print(vlad.name + ' ' + str(vlad.age))

petro = Person('Petro',52)
# petro._Person__set('Petro',52)
print(petro.name + ' ' + str(petro.age))
