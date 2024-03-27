class Ovosh:
	def __init__(self, color,ves):
		self.color = color
		self.ves = ves

	def __str__(self):
		return f'Объект класса Ovosh. Его цвет - {self.color} и его вес - {self.ves}'


morkov = Ovosh('orange',43678)
cucumber = Ovosh('pink',5453)
print(morkov)
print(cucumber)
