# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class person():
	"""создание класса участник"""
	def __init__(self, name, armor, health):
		self.name = name
		self.armor = armor
		self.health = health
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor)
		return desc.title()
class Damage():
	def __init__(self, damage=25):
		self.damage = damage
	def person_damage(self):
		return self.damage

class Player(person):
	"""создание класса игрок"""
	def __init__(self, name, armor, health):
		super().__init__(name, armor, health)
		self.damage = Damage()
		self.__life = int(self.health) + int(self.armor)
	def player_health(self):
		'''здоровье игрока с учетом брони'''
		self.health1 = int(self.health) + int(self.armor)
		return ('Здоровье Player с учетом брони: ' + str(self.health1))
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor + ' удар: '
		 + str(self.damage.person_damage()) + ' здоровье: ' + self.health)
		return desc.title()
	def life_player(self):
		self.__life -= self.damage.person_damage()
		if self.__life <= 0:
			print('Player проиграл.')
		else:
			return ('После атаки, остаток жизни Player: ', self.__life)

class Enemy(person):
	"""создание класса враг"""
	def __init__(self, name, armor, health):
		super().__init__(name, armor, health)
		self.damage = Damage()
		self.__life = int(self.health) + int(self.armor)
	def enemy_health(self):
		'''здоровье врага с учетом брони'''
		self.health2 = int(self.health) + int(self.armor)
		return ('Здоровье Enemy с учетом брони: ' + str(self.health2))
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor + ' удар: '
		 + str(self.damage.person_damage()) + ' здоровье: ' + self.health)
		return desc.title()
	def life_enemy(self):
		self.__life -= self.damage.person_damage()
		if self.__life <= 0:
			print('Enemy проиграл.')
		else:
			return ('После атаки, остаток жизни Enemy: ', self.__life)


player1 = Player('Avalon', '30', '100')
player2 = Enemy('Ninja', '34', '100')
print(player1.description_players())
print(player2.description_players())
print(player2.enemy_health())
print(player1.player_health())
print(player2.life_enemy())
print(player2.life_enemy())
print(player1.life_player())
print(player1.life_player())
print(player1.life_player())
print(player1.life_player())
print(player1.life_player())
print(player1.life_player())