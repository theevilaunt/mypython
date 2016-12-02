class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def car_description(self):
		return (str(self.year) + " " + self.make + " " + self.model).title()

	def odometer_read(self):
		print("odometer: " + self.odometer)

	def odometer_set(self, value):
		if value > self.odometer:
			self.odometer = value

	def odometer_increment(self, value):
		if (value > 0):
			self.odometer += value

class Battery():
	def __init__(self,battery_size=70):
		self.battery_size=battery_size

	def describe_battery(self):
		print("(class) battery size: " + str(self.battery_size) + "-kWh")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		print("range on full charge: " + str(range))

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			#self.describe_battery()

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

t = ElectricCar('tesla','model s',2016)
print(t.description())
t.battery.describe_battery()
t.battery.get_range()
t.battery.upgrade_battery()
t.battery.describe_battery()
t.battery.get_range()