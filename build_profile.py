def build_profile(first,last,**user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

print(build_profile('albert','einstein',location='princeton',field='physics'))
print(build_profile('jeanne','cabeza',location='lima,peru',field='medicine'))

def sandwich(*toppings):
	print("\nsandwich toppings:")
	for topping in toppings:
		print("-" + topping)


sandwich('salami', 'pickles', 'lettuce', 'mustard')

sandwich('peanut butter','jelly')

def make_car(manufacturer, model, **specs):
	print("make a " + model + " by " + manufacturer)
	for key, value in specs.items():
		print("-with " + value + " " + key)


make_car('toyota', 'prius', color='blue', style='hatchback', roof='convertible')

make_car('buick', 'regal', color='red', roof='convertible')
