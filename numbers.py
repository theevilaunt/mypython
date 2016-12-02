for value in range(1,5):
	print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for value in range(1,11):
	squares.append(value**2)

squares = [value**2 for value in range(1,11)]

print(squares)
print(min(squares))
print(max(squares))

list20 = [value for value in range(1,21)]
print(list20)

list100 = [value for value in range(1,101)]
print(list100)

# for number in list100:
# 	print(number)

print(min(list100))
print(max(list100))
print(sum(list100))

listOdd = [value for value in range(1,21,2)]
print(listOdd)

listMult3 = [multiplier*3 for multiplier in range(1,11)]
print(listMult3)

listCubed = [multiplier**3 for multiplier in range(1,11)]
print(listCubed)

for cube in listCubed:
	print(cube)