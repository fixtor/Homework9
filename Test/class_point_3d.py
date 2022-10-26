class Integer:


	@classmethod
	def verify_coord(cls, coord):
		if type(coord) != int:
			raise TypeError('Координаты не int')


	def __set_name__(self, owner, name):
		self.name = "_" + name


	def __get__(self, instance, owner):
		return getattr(instance, self.name)


	def __set__(self, instance, value):
		self.verify_coord(value)
		setattr(instance, self.name, value)



class Point3D:
	x = Integer()
	y = Integer()
	z = Integer()
	d = Integer()

	def __init__(self, x, y, z, do):
		self.x = x
		self.y = y
		self.z = z
		self.d = do


	# @property
	# def x(self):
	# 	return self._x
	#
	#
	# @x.setter
	# def x(self, coord):
	# 	self.verify_coord(coord)
	# 	self._x = coord
	#
	#
	# @property
	# def y(self):
	# 	return self._y
	#
	#
	# @x.setter
	# def y(self, coord):
	# 	self.verify_coord(coord)
	# 	self._y = coord
	#
	#
	# @property
	# def z(self):
	# 	return self._z
	#
	#
	# @x.setter
	# def z(self, coord):
	# 	self.verify_coord(coord)
	# 	self._z = coord


p = Point3D(15,3,5,47)
print(p.__dict__)
