class Cat:
	"__repr__ для отладки, __str__ вывод в консоль"
	def __init__(self, name):
		self.name = name


	def __repr__(self):
		return(f"{self.__class__}:  {self.name}")


	def __str__(self):
		return(f"{self.name}")