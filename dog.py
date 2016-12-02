class Dog():
	"""A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

	def birthday(self):
		self.age = int(self.age) + 1
		print(self.name.title() + " is now " + str(self.age))

f = Dog('spot','12')
print(f.name + " is " + str(f.age))
f.age
f.sit()
f.roll_over()
f.birthday()
f.birthday()

y = Dog('melanie',5)
print(y.name + " is " + str(y.age))
y.sit()
y.roll_over()