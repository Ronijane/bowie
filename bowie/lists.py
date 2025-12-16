# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])
# print(bicycles[0][0])



# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)


cubes = []

for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)