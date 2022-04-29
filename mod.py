#module for area and circumference functions
import math

def house_area():
    length = input('\nWhat is the length of the house in feet? ')
    width = input('\nWhat is the width of the house in feet? ')
    area = int(length) * int(width)
    print(f'\nThank you!\n The house is {area} square feet.')


def circumference():
    diameter = input('In centimeters, what is the diameter of the circle? ')
    cir = int(diameter)*math.pi
    rounded = round(cir)
    print(f'The circumference of the circle is approximately {rounded}cm.')

