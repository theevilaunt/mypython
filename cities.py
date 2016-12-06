cities = {
	'paris': {
		'country': 'france',
		'population': 2.244, 
		'metropolitan': 12.31,
		'nickname': 'la ville des lumieres',
	}
	,'new york': {
		'country': 'usa',
		'population': 8.406,
		'metropolitan': 20.2,
		'nickname': 'big apple'
	}
	,'buenos aires': {
		'country': 'argentina',
		'population': 2.891,
		'metropolitan': 13.694,
		'nickname': 'big apple'
	}
}

def is_number(s):
    try:
        val = int(s)
        return True
    except ValueError:
        return False

for city, info in cities.items():
	print(city)
	for key, value in info.items():
		# print("\t" + key)
		# if is_number(value):
		# 	print("\t\t"  + str(value))
		# else:
		# 	print("\t\t"  + value)
		if is_number(value):
			print("\t" + key + " = " + str(value))
		else:
			print("\t" + key + " = " + value)
	print("\n")




