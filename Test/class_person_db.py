from string import ascii_letters


class Person_db:
	# "хранение данных пользователей
	S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя-'
	S_RUS_UPPER = S_RUS.upper()


	def __init__(self, fio, age, number, comment):

		self.verify_fio(fio)


		self.__fio = fio.split()
		self.age = age
		self.number = number
		self.comment = comment


	@classmethod
	def verify_fio(cls, fio):
		if type(fio) != str:
			raise TypeError('ФИО должно str')

		f = fio.split()
		if len(f) !=3:
			raise TypeError('Неверный формат ФИО')

		letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
		for s in f:
			if len(s) < 1:
				raise TypeError('в ФИО должен быть символ')
			if len(s.strip(letters)) != 0:
				raise TypeError('в ФИО должен использоваться только буквы символы, дефис')


	@classmethod
	def verify_age(cls, age):
		if type(age) != int or age > 100 or age < 14:
			raise TypeError('Возраст должен число и диапазон от 14 до 100')


	@classmethod
	def verify_number(cls, number):
		if type(number) != str or len(number) != 12 or number[0] != '+':
				raise TypeError('Номер должен быть 10 цифр и в формате строки c префиксом "+"')


	@classmethod
	def verify_comment(cls, comment):
		if type(comment) != str:
			raise TypeError('Комментарий должен быть str')


	@property
	def fio(self):
		return self.__fio


	@fio.setter
	def fio(self, fio):
		self.verify_fio(fio)
		self.__fio = fio


	@property
	def age(self):
		return self.__age


	@age.setter
	def age(self, age):
		self.verify_age(age)
		self.__age = age


	@property
	def number(self):
		return self.__number


	@number.setter
	def number(self, number):
		self.verify_number(number)
		self.__number = number


	@property
	def comment(self):
		return self.__comment


	@comment.setter
	def comment(self, comment):
		self.verify_comment(comment)
		self.__comment = comment



pax = Person_db('ИВанов Иван Иванович', 15, '+79112651565', '1')
pax1 = Person_db('Петров Петр Васильвеич', 45, '+78129990009', '2')

print(pax.fio,
      pax.age,
      pax.number,
      pax.comment,'\n',
	  pax1.fio,
      pax1.age,
      pax1.number,
      pax1.comment)

