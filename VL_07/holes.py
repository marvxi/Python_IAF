import numpy as np
class Circle:


    def __init__(self,radius):
        self.radius = radius
        self.area = 0.0
        self.cirumference = 0.0
        self._area()
        self._circumference()

    def _area(self):
        area = np.pi * self.radius ** 2
        self.area = area


    def _circumference(self):
        cirumference = 2 * np.pi * self.radius
        self.cirumference = cirumference