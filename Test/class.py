from accessify import private, protected



class Point:
	"Класс для создания точек на плоскости"

	MIN_COORD = 0
	MAX_CORD = 100


	@classmethod
	def validate(cls, arg):
		return cls.MIN_COORD <= arg <= cls.MAX_CORD


	__instance = None

	def __new__(cls, *args, **kwargs):
		print('Вызов __NEW__' +str(cls))
		return super().__new__((cls))


	def __init__(self, x, y, z):
		self.__x = self.__y = self.__z = 0
		if self.validate(x) and self.validate(y) and self.validate(z):
			if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
				self.__x = x
				self.__y = y
				self.__z = z


	@classmethod
	def __check_value(cls, arg):
		return type(arg) in (int, float)


	def set_coords(self, x: object, y: object, z: object) -> object:
		if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
			self.__x = x
			self.__y = y
			self.__z = z
		else:
			raise ValueError('int, float, complex')


	def get_coords(self):
		return [self.__x, self.__y, self.__z]


	@staticmethod
	def norm3(__x, __y, __z):
		return __x*__x*__x+__y*__y*__y+__z*__z*__z



pt = Point(30, 20, 10)

lst = (pt.get_coords())
print(lst)

for j in range(0, len(lst)-1):
	for i in range(0, len(lst)-1):
		temp = 0
		if lst[i] >= lst[i+1]:
			temp = lst[i]
			lst[i] = lst[i+1]
			lst[i+1] = temp
	print(lst)