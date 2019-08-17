class Person:
	name = 'Ivan'
	age = 10

	def __set(self, name, age):
		self.name = name
		self.age = age

class Student (Person):
	course = 1

igor = Student()
igor._Person__set('Igor', 19)
print(igor.name)
print(igor.course)
igor.course = 2
print(igor.course)

vlad = Person()
vlad._Person__set("Vlad", 25)
print(vlad.name + ' ' + str(vlad.age))

petro = Person()
petro._Person__set('Petro',52)
print(petro.name + ' ' + str(petro.age))
