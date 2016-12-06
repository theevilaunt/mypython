while True:
	cars_offered = ['lexus','ford','honda']
	prompt = "rental car type desired (or q to quit): "
	choice = input(prompt)
	if choice == 'q':
		break
	if choice in cars_offered:
		break
	else:
		print("cars offered limited to: ")
		print(cars_offered)
if choice != 'q':
	print("your " + choice + " is ready")