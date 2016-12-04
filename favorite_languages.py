from collections import OrderedDict

fl = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in sorted(fl.keys()):
	print ("sorted: " + name + ": " + fl[name])

for value in set(fl.values()):
#for value in fl.values():
	print(value)

#print(sorted(fl, key=fl[0])

for k,v in fl.items():
	print(k.title() + "'s favorite lang is " + v.title() + ".")

for name in fl.keys():
	print(name.title())

friends = ['phil','sarah']

for name in fl:
	#print(fl[name])
	if name in friends:
		print (name.title() + "'s favorite language is: " + fl[name].title())

pollee = 'erin'
if pollee not in fl:
	print(pollee + " please take our poll")


