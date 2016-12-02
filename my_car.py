from car import Car

new_car = Car('audi','a4',2016)

print(new_car.car_description())

new_car.odometer_set(23)
new_car.odometer_read()