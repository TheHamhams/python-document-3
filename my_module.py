from math import pi

def house_sqft():
    length = int(input('What is the length of your house? '))
    width = int(input('What is the width of your house? '))
    return f'Your house is {length * width}sqft'

def circ():
    r = float(input('What is the radius of your circle?'))
    return 2*pi*r