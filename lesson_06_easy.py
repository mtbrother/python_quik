# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar():
	'''класс городской автомобиль'''
	def __init__(self, name, color, speed, is_police=False):
		self.name = name
		self.color = color
		self.speed  = speed
		self.is_police = is_police
		print('Автомобиль ' , self.name, self.color, self.speed)
		if is_police == True:
			print('Уступите дорогу!')

	def go(self):
		"""Автомобиль поедет"""
		print(self.name + ' поехала')
	def stop(self):
		"""Автомобиль остановится"""
		print(self.name + ' остановилась')
	def turn(self, direction):
		self.direction = direction
		"""Автомобиль поварачивает"""
		print(self.name + ' повернула', direction)

class SportCar():
	'''класс спортивный автомобиль'''
	def __init__(self, name, color, speed, is_police=False):
		self.name = name
		self.color = color
		self.speed  = speed
		self.is_police = is_police
		print('Автомобиль ' , self.name, self.color, self.speed)
		if is_police == True:
			print('Уступите дорогу!')

	def go(self):
		"""Автомобиль поедет"""
		print(self.name + ' поехала')
	def stop(self):
		"""Автомобиль остановится"""
		print(self.name + ' остановилась')
	def turn(self, direction):
		self.direction = direction
		"""Автомобиль поварачивает"""
		print(self.name + ' повернула', direction)

class WorkCar():
	'''класс спецтранспорт'''
	def __init__(self, name, color, speed, is_police=False):
		self.name = name
		self.color = color
		self.speed  = speed
		self.is_police = is_police
		print('Автомобиль ' , self.name, self.color, self.speed)
		if is_police == True:
			print('Уступите дорогу!')

	def go(self):
		"""Автомобиль поедет"""
		print(self.name + ' поехала')
	def stop(self):
		"""Автомобиль остановится"""
		print(self.name + ' остановилась')
	def turn(self, direction):
		self.direction = direction
		"""Автомобиль поварачивает"""
		print(self.name + ' повернула', direction)

class PoliceCar():
	'''класс полицейский автомобиль'''
	def __init__(self, name, color, speed, is_police=True):
		self.name = name
		self.color = color
		self.speed  = speed
		self.is_police = is_police
		print('Автомобиль',self.name, self.color, self.speed)
		if is_police == True:
			print('Уступите дорогу!')

	def go(self):
		"""Автомобиль поедет"""
		print(self.name + ' поехала')
	def stop(self):
		"""Автомобиль остановится"""
		print(self.name + ' остановилась')
	def turn(self, direction):
		self.direction = direction
		"""Автомобиль поварачивает"""
		print(self.name + ' повернула', direction)

#car1 = TownCar('mazda', 'black', '60 km/h')
#car1.turn('направо')
#car2 = SportCar('porshe 911', 'red', '200 km/h')
#car2.go()
#car3 = WorkCar('KamaZ', 'green', '0 km/h')
#car3.stop()
#car4 = PoliceCar('ford', 'white', '100 km/h')
#car4.turn('налево')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class CarsTrucks():
	def __init__(self, name, color, speed, is_police=True):
		self.name = name
		self.color = color
		self.speed  = speed
		self.is_police = is_police
		print('Автомобиль',self.name, self.color, self.speed)
		if is_police == True:
			print('Уступите дорогу!')

	def go(self):
		"""Автомобиль поедет"""
		return self.name + ' поехала'
	def stop(self):
		"""Автомобиль остановится"""
		return self.name + ' остановилась'
	def turn(self, direction):
		self.direction = direction
		return self.name + ' повернула' + ' ' + direction

class TownCar(CarsTrucks):
	"""класс городской автомобиль"""
	def __init__(self, name, color, speed, is_police=True):
		super().__init__(name, color, speed, is_police=False)

class SportCar(CarsTrucks):
	"""класс спортивный автомобиль"""
	def __init__(self, name, color, speed, is_police=True):
		super().__init__(name, color, speed, is_police=False)

class WorkCar(CarsTrucks):
	"""класс спецтехника"""
	def __init__(self, name, color, speed, is_police=True):
		super().__init__(name, color, speed, is_police=False)

class PoliceCar(CarsTrucks):
	"""класс полицейский автомобиль"""
	def __init__(self, name, color, speed, is_police=True):
		super().__init__(name, color, speed, is_police=True)

# car1 = TownCar('Honda', 'brown', '77 km/h')
# print(car1.turn("влево"))
# car2 = SportCar('Ferarry', 'red', '220 km/h')
# print(car2.go())
# car3 = WorkCar('Tatra', 'blue', '0 km/h')
# print(car3.stop())
# car4 = PoliceCar('Ford', 'white', '100 km/h')
# print(car4.go())