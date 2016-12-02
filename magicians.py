magicians1 = ['alice','david','carolina']

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
		#print("can't wait to see the next one, " + magician.title() + ".\n")

def make_great(list):
	index = 0
	for element in list:
		list[index] = 'the Great ' + element
		index = index + 1
	return(list)


show_magicians(magicians1)
magicians2 = make_great(magicians1[:])
print("\nmagicians1:")
show_magicians(magicians1)
print("\nmagicians2 (modified):")
show_magicians(magicians2)

# parrots = ['cockatiel','parrotlet','maccaw']

# for parrot in parrots:
# 	print(parrot + " is a type of bird")

# print("they are all parrots")