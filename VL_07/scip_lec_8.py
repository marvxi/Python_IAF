import numpy as np
from function import *
import pytest
from copy import copy

radius_circel_1 = 0.7

# print(f'radius: {area_circle(radius_circel_1)}, circumference_circle: {circumference_circle(radius_circel_1)}')
#
# areaCircel_1 = area_circle(radius=radius_circel_1)
# circumference_circle = circumference_circle(radius=radius_circel_1)
#
# circel_1 = [radius_circel_1, areaCircel_1,circumference_circle]
#
# edge_square_1 = 0.5
# area_square_1 = area_square(edge=edge_square_1)

from holes import *

def test_circel_addition():

    circle1 = Circle(radius=0.5)

    circle2 = Circle(radius=0.7)

    print(circle1.radius)
    print(circle1.area)
    print(circle1.cirumference)
    print("------------------------")
    print(circle2.radius)
    print(circle2.area)
    print(circle2.cirumference)
    print("--------------------------")
    circle3 = circle1 + circle2
    print(circle3.radius,circle3.area,circle3.cirumference)

    #print(np.isclose(circle3.area,circle1.area + circle2.area)) # Vergleicht die Werte, kann zur Validierung verwendet werden

    assert np.isclose(circle3.area,circle1.area + circle2.area), 'Addition der Klasse Circel ergbit falsches Ergebnis' # Gibt Fehler aus wenn etwas falsch ist.

def test_square_class():

    circelSquare = Square(radius=0.5)
    print(circelSquare.square)

    assert np.isclose(circelSquare.square, circelSquare.radius**2+2),'Quadrien nicht geglückt'


#test_square_class()

# def test_update_circle_radius():
#     circel = Circle(radius=0.5)
#     area = copy(circel.area)
#     cirum = copy(circel.cirumference)
#
#     circel = 0.7
#     area2 = copy(circel.area)
#     cirum2 = copy(circel.circumference)
#
#     assert not np.isclose(area,area2), "The area is not supposed to be identical"
#     assert not np.isclose(cirumference, cirumgerence2),"The circum is not supposed"

