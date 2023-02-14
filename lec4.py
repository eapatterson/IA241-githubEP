'''
lec4
dict and tuple
'''

my_tuple = ('a','b','c','d','e')

#my_tuple[0]='f'
print( my_tuple[0:2])

my_car = {
     'color':'purple',
     'maker': 'toyota',
     'year': 2015
         }
print(my_car)
print(my_car['year'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('year'))

my_car['model'] = 'Corolla'
my_car['year'] = 2020
print(my_car)
print( len(my_car))
print('color' in my_car)
