def get_formatted_name(first, last, middle=''):
	"""full name in title case"""
	if middle:
		return (first + ' ' + middle + ' ' + last).title()
	else:
		return (first + ' ' + last).title()

print(get_formatted_name('jimi','hendrix', 'lee'))
print(get_formatted_name('jimi','hendrix'))

def build_person(first, last, age=''):
	"""return dictionary"""
	if age:
		return {'first':first,'last':last, 'age':age}
	else:
		return {'first':first,'last':last}

print(build_person('jimi','hendrix',27))