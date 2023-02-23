'''
lab5
if statement
'''

#3.1
alien_color='green'
if alien_color=='green':
    print('you got 5 points')
    
#3.2
alien_color='red'

if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points')
    
#3.3
favorite_fruit = ['apple','raspberry','pineapple']

if 'orange' in favorite_fruit:
    print('you really like orange')
    
if 'raspberry' in favorite_fruit:
    print('you really like raspberry')

if 'pineapple' in favorite_fruit:
    print('you really like pineapple')

#3.4

age=20

if age < 10:
    print('kid')
elif age < 20:
    print('teenager')
else:
    print('adult')
    if age > 65 :
        print('elder')
     
 