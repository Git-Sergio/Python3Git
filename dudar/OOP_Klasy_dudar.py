class Person:
	name = 'Ivan'
	age = 10

	def set(self, name, age):
		self.name = name
		self.age = age


vlad = Person()
vlad.set("Vlad", 25)
print(vlad.name + ' ' + str(vlad.age))

petro = Person()
petro.set('Petro',52)
print(petro.name + ' ' + str(petro.age))



vlad = Person()
vlad.name = "Vlad"
print(vlad.name)

ivan = Person()
print(ivan.name)

ivan = Person()
ivan.age = 45
print(ivan.age)