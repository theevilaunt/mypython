class Person():
	def __init__(self, first, last, age, city):
		self.first = first
		self.last = last
		self.age = age
		self.city = city
	def describe(self):
		print(self.first + " " + 
			  self.last + 
			  " age " + str(self.age) + 
			  " lives in " + self.city
		)
	def name(self):
		return(self.first + " " + self.last)

who = []

me = Person('heidi','lastName',59,'cardiff')
me.describe()
who.append(me)

myhusband = Person('steve', 'lastName', 62, 'cardiff')
myhusband.describe()
who.append(myhusband)

mydaughter = Person('kamalia', 'lastName', 21, 'rochester')
mydaughter.describe()
who.append(mydaughter)

for person in who:
	print(person.name())

favorite_number = { me: 5, myhusband: 6}
print(me.name() + "'s favorite number is " + str(favorite_number[me]))

