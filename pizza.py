def make_pizza(size, *toppings):
	"""list of toppings requested"""
	print("make a " + str(size) + '" pizza with toppings:')
	for topping in toppings:
		print("-" + topping)
	print("\n")