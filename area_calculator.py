"""
area_calculator.py
calculates area of triangle, circle, or rectangle based on user input
"""

from math import pi

print("Area Calculator is Running")

shape_choice = input('Choose a shape. Enter C for circle, T for triangle, or R for rectangle: ')

if shape_choice == 'C':
    circle_radius = float(input('Enter radius: '))
    area = pi * circle_radius ** 2
    print (area)
elif shape_choice == 'T':
    triangle_base = float(input('Enter base: '))
    triangle_height = float(input('Enter height: '))
    area = triangle_base * triangle_height * .5
    print (area)
elif shape_choice == 'R':
    rectangle_width = float(input('Enter width: '))
    rectangle_height = float(input('Enter height: '))
    area = rectangle_width * rectangle_height
    print (area)
else:
    print ('Invalid Input.')
