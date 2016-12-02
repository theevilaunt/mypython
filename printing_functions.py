def print_models(unprinted, completed):
	while unprinted:
		completed.append(unprinted.pop())

def show_lists(unprinted, completed, when):
	print(when + ": unprinted, completed")
	print(unprinted)
	print(completed)	