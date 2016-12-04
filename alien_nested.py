alien_0 = {
	'color': 'green',
	'points': 5
}
alien_1 = {
	'color': 'yellow',
	'points': 10
}
alien_2 = {
	'color': 'red',
	'points': 15
}

aliens = []
aliens = [ alien_0, alien_1, alien_2 ]

aliens = []
aliens.append(alien_0)

def string_status(mylist):
	print(str(len(mylist)))
	print(mylist)
	#print("\n")

string_status(aliens)
aliens.append(alien_1)
string_status(aliens)
aliens.append(alien_2)
string_status(aliens)

print(len(aliens))

for alien in aliens:
	print(alien)

# for number in range(1,16):
# 	print(number)