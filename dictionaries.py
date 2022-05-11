car = {
    'make':'Nissan',
    'model':'Altima',
    'miles':1000,
    'new_condition':True,
    'engine':'V6'
}
print(car['make'])
car['color']='silver'
print(car)
car['engine']='V4'
print(car)
del car['color']
print(car)

for key in car.keys():
    print(key)

for value in car.values():
    print(value)

for key,value in car.items():
    print(key,value)

