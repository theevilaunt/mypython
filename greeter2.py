def get_formatted_name(first,last):
	"""return full formatted name"""
	return(first + " " + last).title()


while True:
	print("\nInput Names\n(enter 'q' to quit)")
	first = input("First: ")
	if first[0].lower() == 'q':
		break
	last = input("Last: ")
	if last[0].lower() == 'q':
		break
	print("Hello " + get_formatted_name(first,last) + "!")