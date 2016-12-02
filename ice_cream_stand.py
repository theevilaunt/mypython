from restaurant import Restaurant

class Ice_Cream_Stand(Restaurant):
	def __init__(self, name, cuisine):
		super().__init__(name,cuisine)
		self.flavors = ['vanilla','chocolate','strawberry']

	def describe_flavors(self):
		print("serves flavors:")
		for flavor in self.flavors:
			print(flavor)

i = Ice_Cream_Stand("dairy queen", "ice cream")

i.describe()
i.describe_flavors()

