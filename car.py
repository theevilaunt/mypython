class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_description(self):
		return (str(self.year) + " " + self.make + " " + self.model).title()

	def get_odometer(self):
		print("odometer: ", self.odometer)

	def set_odometer(self, value):
		if self.odometer > value:
			print("milleage rollback not permitted")
		else:
			self.odometer = value

	def increment_odometer(self, value):
		if value < 0:
			print("milleage rollback not permitted")
		else:
			self.odometer += value


my_car = Car('audi', 'a4', 2016)

print(my_car.get_description())

my_car.set_odometer(23)
my_car.get_odometer()
my_car.set_odometer(50)
my_car.get_odometer()
my_car.set_odometer(25)
my_car.increment_odometer(100)
my_car.get_odometer()