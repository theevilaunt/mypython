prompt = "enter name to personalize\n"
prompt += "name: "

name = input(prompt)

age = input("age: ")
print(age)

if age.find("."):
	age = float(age)
else:
	age = int(age)

print("age: " + str(age))