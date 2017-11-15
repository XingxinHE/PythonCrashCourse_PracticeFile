# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:22:17 2017

@author: Administrator
"""

place_for_vacation = ['Vancouver','Basel','Melbourne','New York','Shanghai']
print('The first three items in the list are:')
print(place_for_vacation[:4])

pizza = ['a pizza','b pizza','c pizza']
friendPizza = pizza[:]
pizza.append('x pizza')
friendPizza.append('y pizza')

print('My favorite pizzas are: ')
for mypizza in pizza:
    print('*'+mypizza)

print('\n')

print("My friend's favorite pizzas are: ")
for myFriendpizza in friendPizza:
    print('*'+myFriendpizza)

