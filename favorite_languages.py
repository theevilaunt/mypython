from collections import OrderedDict

class FavoriteLanguages ():
	def __init__(self, first_name, languages):
		self.first_name = first_name
		self.languages = languages

	def one_entry(self):
		print(self.first_name + " likes ")
		for language in self.languages:
			print("\t" + language)

fl_class = []

fl_class.append(FavoriteLanguages('jen',['python', 'c', 'ruby']))
fl_class.append(FavoriteLanguages('sarah','c'))
fl_class.append(FavoriteLanguages('edward',['ruby','python','c#']))
for entry in fl_class:
	print(entry.one_entry())

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

pollees = ['erin','jack','liz','edward','marion']

for pollee in pollees:
	if pollee not in fl.keys():
		print(pollee + " needs to take poll")
	else:
		print(pollee + " took poll")


