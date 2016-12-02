first = "ada"
last = "lovelace"

name1 = first + " " + last
print(name1.title())
print(name1.upper())

name2 = "ADA LOVELACE"
print(name2.lower())

print("Hello " + name1.title() + "!")

print("Languages:\n\tPython\n\tC\n\tJavascript")

fav = "python   "
print(fav + "!")
print(fav.rstrip() + "!")
print("before rstrip: " + fav + "!")
fav = fav.rstrip()
print("after strip: " + fav + "!")

fav2 = "    python     "
print("before strip: !" + fav2 + "!")
print("after strip: !" + fav2.strip() + "!")

name3 = "heidi"
tmp = "experiment: " + name3 + " test"
print(tmp)

test2 = "\tbogus\t"
print("!" + test2 + "!")
print("!" + test2.strip() + "!")
