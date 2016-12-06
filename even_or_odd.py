while True:
	number = input("enter # or 'q' to quit: ")
	if number == 'q':
		break
	number = int(number)
	if number % 2 == 0:
		print(str(number) + " is even")
	else:
		print(str(number) + " is odd")