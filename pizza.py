def make_pizza(size, *toppings):
	"""list of toppings requested"""
	print("make a " + str(size) + '" pizza with toppings:')
	for topping in toppings:
		print("-" + topping)
	print("\n")

pizza = {
	'size': 'medium',
	'crust':'thick',
	'toppings': ['mushrooms','extra cheese']
}

class Pizza():
	def __init__(self, size, crust, toppings):
		self.size = size
		self.crust = crust
		self.toppings = toppings

	def describe(self):
		print(self.size + " pizza with " + self.crust + " crust & toppings: ")
		for topping in self.toppings:
			print("\t" + topping)


p = Pizza('medium','thick',['mushrooms','pineapple'])
p.describe()