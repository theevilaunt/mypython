class User():
	def __init__(self,first,last):
		self.first = first
		self.last = last
		self.username = first[0] + last

	def describe_user(self):
		print("user " + self.first + " " + self.last + ": " + self.username)


u = User("heidi", "keller")

u.describe_user()

x = User("jan",'brown')

x.describe_user()