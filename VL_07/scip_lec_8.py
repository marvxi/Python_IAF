import numpy as np
from function import *

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

from holes import Circle

circle1 = Circle(radius=0.5)

circle2 = Circle(radius=0.7)

print(circle1.radius)
print(circle1.area)
print(circle1.cirumference)
print("------------------------")
print(circle2.radius)
print(circle2.area)
print(circle2.cirumference)