CityCountry = {}

while True:
	print("type 'q' to quit")
	city = input("city? ")
	if city[0] == 'q':
		break
	country = input("country? ")
	if country[0] == 'q':
		break
	CityCountry[country] = city

print(CityCountry)

for element in CityCountry:
	print(CityCountry[element] + " is in " + element)