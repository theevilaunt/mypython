class Restaurant():
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe(self):
		print(self.name + " serves " + self.cuisine)

	def open_restaurant(self):
		print(self.name + " is now open.")


# p = Restaurant('panera', 'soup and salads')
# r = Restaurant('mcdonalds', 'fast food')
# l = Restaurant('pollo loco', 'chicken')

# rlist = [p, r, l]

# for rest in rlist:
# 	print(rest.name)
# 	print(rest.cuisine)
# 	rest.describe()
# 	rest.open_restaurant()
# 	print("\n")