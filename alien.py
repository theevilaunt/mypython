class Alien():
	def __init__(self, characteristics):
		self.characteristics = characteristics

	def move_alien(self):
		if self.characteristics['speed'] == 'slow':
			self.characteristics['x_increment'] = 1
		elif self.characteristics['speed'] == 'medium':
			self.characteristics['x_increment'] = 2
		else: # alien['speed'] == 'fast':
			self.characteristics['x_increment'] = 3
		self.characteristics['x_position'] += self.characteristics['x_increment']

	def show_characteristic(self, type):
		print(type + " is " + str(self.characteristics[type]))

	def show_all_characteristics(self):
		for characteristic in self.characteristics:
			self.show_characteristic(characteristic)
		print("\n")

	def set_characteristic(self, type, value):
		old_value = self.characteristics[type]
		self.characteristics[type] = value
		print(type + " changed from " + str(old_value) + " to " + str(value))

	def del_characteristic(self, type):
		del(self.characteristics[type])
		print("\nafter deletion of " + type)
		self.show_all_characteristics()


myAlien = {
	'color': 'green',
	'points': 5,
	'x_position': 0,
	'y_position': 25,
	'speed': 'medium',
	'x_increment': 0,
}

alien_0 = Alien(myAlien)
alien_0.show_all_characteristics()
alien_0.show_characteristic('color')
alien_0.set_characteristic('color','yellow')
alien_0.move_alien()
alien_0.show_characteristic('x_increment')
alien_0.show_characteristic('x_position')
alien_0.del_characteristic('color')


# new_points = alien_0['points']
# print("You earned " + str(alien_0['points']) + " points!")

# print(alien_0)
# alien_0['color'] = "yellow"

# print(alien_0)

# move_alien(alien_0)

# print(alien_0)

