from abc import ABC, abstractmethod
from math import floor

class Character(ABC):
	def __init__(self, name, level, strengh=8, dixterity=8, constitution=8, intilligence=8, wisdom=8, charisma=8, max_xp, hp, armour_class, initiative):
		self.name = name
		self.level = level
		self.strengh = strengh
		self.dixterity = dixterity
		self.constitution = constitution
		self.intilligence = intilligence
		self.wisdom = wisdom
		self.charisma = charisma
		self.max_xp = 10 + floor((self.constitution + 10) / 2) + randint(1, 11) + 3
		self.hp = self.max_xp
		self.armour_class = 15 + floor((self.dixterity + 10) / 2)
		self.initiative = randint(1, 21) + floor((self.dixterity + 10) / 2)

	def attack(self):
		return randint(1, 13) + floor((self.strengh - 10) / 2)

	def save_throw(self, attribute):
		return randint(1, 21) + floor((self.max_xp + 10) / 2)


	@abstractmethod
	def perk(self):
		pass

class Hero(Character):
	def perk(self):
		return randint(1, 21) + floor((self.wisdom - 10 ) / 2)

class Dragon(Character):
	def perk(self):
		return randint(1, 17) + floor((self.hp + 10) / 2)
