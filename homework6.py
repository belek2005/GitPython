from math import pi
from abc import ABC, abstractmethod

class Figure():
	@abstractmethod
	def draw(self):
		print("Квадрат нарисован")

a = Figure()
a.draw()

class Square(Figure):
	@staticmethod
	def square():
		S = pi*a^2
b = Square()
b.square()

class Round(Figure):
	def draw(self):
		super().draw()
		print('Круг нарисован')
	def __square():
		S = pi*a^2

c = Round()
c.draw()
c._Round__square()
c.__square()
