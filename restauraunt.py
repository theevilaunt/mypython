class Restaurant():
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.served = 0

	def describe(self):
		print("restaurant " + self.name + " serves " + " food.")

	def open(self):
		print("restaurant " + self.name + " is now open.")

	def set_served(self, value):
		if value > 0:
			self.served = value

	def increment_served(self, value):
		if value > 0:
			self.served += value

	def has_served(self):
		print("restaurant has served " + str(self.served))

r = Restaurant("mcdonalds","fast food")
r.describe()
r.open()
r.has_served()
r.set_served(23)
r.has_served()
r.increment_served(5)
r.has_served()