class Person:


	def __init__(self, name, old):
		self.__name = name
		self.__old = old


	@property
	def old(self):
		return self.__old


	@old.setter
	def old(self, old):
		self.__old = old


	@old.deleter
	def old(self):
		del self.__old





p = Person('Сергей', 35)
p1 = Person('Иван', 12)
p1.old = 12
print(p.old)
print(p1.old)
del p.old

print(p.__dict__)
print(p1.__dict__)