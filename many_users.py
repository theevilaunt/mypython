users = {
	'aeinstein': {
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},
	'mcurie': {
		'first':'marie',
		'last':'curie',
		'location':'paris',
	},	
}

for user, info in users.items():
	full = info['first'] + " " + info['last']
	print(full + " resides in " + info['location'])