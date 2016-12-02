def greet_user(username):
	print("Hello " + username.title() + "!")

greet_user('heidi')

def describe_pet(pet_name, animal='dog'):
	"""Display pet info"""
	print("\nI have a " + animal+ ".")
	print("My " + animal + "'s name is " + pet_name.title() + ".")

describe_pet("bird","ciel")
describe_pet("dog","kiki")
describe_pet(pet_name='warlock', animal='horse')
describe_pet(pet_name='kioshi')
#describe_pet("ab","b","c")

def make_shirt(size="large",msg="I love Python"):
	print("construct a size %s shirt with message '%s'" % (size,msg))

make_shirt(12, "bogus")
make_shirt(12)
make_shirt(msg="you've got to be kidding!",size=14)
make_shirt("medium")

def describe_city(city, country="the usa"):
	print("\n%s is in %s" % (city,country))

describe_city("buenos_aires", "argentina")
describe_city("los angeles")
describe_city(country="switzerland", city="basel")

