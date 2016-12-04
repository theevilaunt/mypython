a = [1,4,13,5,8,10]

print(a)
print(sorted(a))
print(a)
a.sort(reverse=True)
print("after calling a.sort()")
print(a)

tup = (21, 9,3,6,12)

print(sorted(tup))

def getKey(item):
	return(item[1])

l = [
	[2,3],
	[6,7],
	[3,34],
	[24,64],
	[1,43],
]

print(l[0])

print(sorted(l, key=getKey))

class Custom():
	def __init__(self,name,number):
		self.name = name
		self.number = number
	def __repr__(self):
		return '{}:{}{}'.format(
			self.__class__.__name__,
			self.name,
			self.number
		)
	def __cmp__(self,other):
		if hasattr(other, 'number'):
			return self.number.__cmp__(other.number)

custom_list = [
	Custom('object',99),
	Custom('michael',1),
	Custom('thedore',59),
	Custom('life',42),
]

def getKey(custom):
	return custom.number

#print(sorted(custom_list, key=getKey))
print(sorted(custom_list))