import numpy as np
class Circle:


    def __init__(self,radius):
        self._radius = 0.0

        self.area = 0.0
        self.cirumference = 0.0
        self._area()
        self._circumference()

    def __repr__(self):
        representation = "Hole of type circle with radius: " + str(self.radius) + " mm" # Klassen können im debugger beschrieben werden
        return representation

    def __add__(self, other): # other ist zweite Instanz die hinzugefügt wird
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area/np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle


    def _area(self):
        area = np.pi * self.radius ** 2
        self.area = area


    def _circumference(self):
        cirumference = 2 * np.pi * self.radius
        self.cirumference = cirumference

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._value = value
        self.area()
        self._circumference()

class Square:

    def __init__(self,radius):
        self.radius = radius
        self.square = 0.0
        self._square()

    def _square(self):
        square = self.radius**2
        self.square = square

