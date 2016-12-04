rivers = {
	'nile': 'egypt',
	'amazon': 'many countries in south america',
	'santa margarita':'san diego cty north',
	'san luis rey':'oceanside',
	'san dieguito river': 'del mar',
	'san diego river': 'san diego',
	'sweetwater river': 'national city and chula vista',
	'otay river': 'border',

}

for key, value in rivers.items():
	print(key + " runs thru " + value)

for river in rivers:
	print(river)

for where in sorted(set(rivers.values())):
	print(where)