while True:
	prompt = "how many in party ('q' to quit)? "
	reply = input(prompt)
	if reply == 'q':
		break
	how_many = int(reply)
	if how_many <= 8:
		print("table is ready.")
	else:
		print("you will have to wait")
