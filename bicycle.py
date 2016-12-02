bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])
print(bicycles[-2])

bicycles[0] = 'honda'
print(bicycles)

bicycles.append('schwinn')
print(bicycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('bmw')
print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

pop_cycle = motorcycles.pop()
print(motorcycles)
print(pop_cycle)

motorcycles.remove('honda')
print(motorcycles)

invitees = ["joe", "jane", "jim"]
for invitee in invitees:
	print("%s, you are invited!" % invitee.title())

declining = "joe"
invitees.remove(declining)

print("new list without " + declining)
for invitee in invitees:
	print("%s, you are invited!" % invitee.title())

invitees.insert(0, "bruce")
invitees.insert(len(invitees), "ben")

print("new list with bigger table")
for invitee in invitees:
	print("%s, you are invited!" % invitee.title())
print(invitees)

counter = 0
while (len(invitees) > 2):
	disinvited = invitees.pop()
	print("%s, you are disinvited!" % disinvited.title())
	counter = counter + 1
	if counter > 10:
		exit()
print("total invitees = " + str(len(invitees)))

print(invitees)
del invitees[1]
del invitees[0]
print(invitees)
# del invitees[-1]

