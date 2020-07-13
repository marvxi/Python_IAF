import cv2
import numpy as np
import matplotlib.pyplot as plt
class HoleDetection():

    def __init__(self, filename, filepath):
        self._filename = filename
        self._filepath = filepath
        self._image = None
        self._holeList = []
        self._list_radius_intended = []


    @property
    def Filename(self):
        return self._filename

    @property
    def Filepath(self):
        return self._filepath

    @property
    def Image(self):
        if self._image is None:

            image = cv2.imread(self._filepath + self._filename, 1)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self._image = cv2.medianBlur(image_gray, 5)
        return self._image

    @property
    def holeList(self):
        if not self._holeList:
            circles = cv2.HoughCircles(self._image,cv2.HOUGH_GRADIENT, 1, 150, param1=500, param2=15, minRadius=0,
                                        maxRadius=50)

        radiiPx = circles[0,:,2]
        radiiMM = radiiPx / 75.0

        if not self._list_radius_intended:
            print('Please write down the intended radii separated by spaces in micrometer')
            list_radius_intended = [int(x)/1000 for x in input().split()]
        else:
            list_radius_intended = self._list_radius_intended

        for radius in radiiMM:
            circle = Circle(radius=radius)
            circle.radius_intended = list_radius_intended
            self._holeList.append(circle)

        return self._holeList

    def plotRadii(self):
        radiiList = []
        radiiIntendedList = []

        for hole in self._holeList:
            radiiList.append(hole.radius)
            radiiIntendedList.append(hole.radius_intended)

        radiiArray  = np.asarray(radiiList)
        radiiIntendedArray = np.asarray(radiiIntendedList)

        plt.plot(radiiIntendedArray,radiiArray,'o')
        plt.show()

class Hole:
    """
    Hole describes a general hole
    """

    name = 'Hole'
    class_counter = 0

    def __init__(self):
        """
        Initialising an instance of the class hole sets the centre point of the hole at the coordinates (0/0)
        """
        Hole.class_counter += 1
        self._centre_point = (0, 0)
        pass

    @property
    def centre_point(self):
        """
        The centre point of the hole
        :return: _centre_point: tuple
        """
        return self._centre_point

    @centre_point.setter
    def centre_point(self, value):
        """

        :param value: tuple
        """
        self._centre_point = value


class Circle(Hole):
    """
    This class represents a circle
    """

    def __init__(self, radius):
        """

        :param radius: float
        """
        # Initialise protected attributes
        super().__init__()
        self._radius = 0.0
        self._radius_intended = 0.0

        # Set initial values
        self.radius = radius

    def __repr__(self):
        """
        How python shows an instance of type Circle
        :return: representation_string: str
        """
        representation_string = "Hole of type circle with radius: " + str(self._radius) + "mm"
        return representation_string

    def __add__(self, other):
        """
        Two circles are added by adding their area
        :param other: Circle
        :return: new_circle: Circle
        """
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area/np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle

    @property
    def radius(self):
        """
        The radius of the circle
        :return: _radius: float
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        The radius of the circle
        :param value: float
        """
        self._radius = value

    @property
    def area(self):
        """
        The area of the circle
        :return: area: float
        """
        area = np.pi * self._radius ** 2
        return area

    @property
    def circumference(self):
        """
        The circumference of the circle
        :return: circumference: float
        """
        circumference = 2 * np.pi * self._radius
        return circumference

    @property
    def radius_intended(self):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :return: _radius_intended: float
        """
        return self._radius_intended

    @radius_intended.setter
    def radius_intended(self, value):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :param value: float
        """
        array_radii_intended = np.asarray(value)
        idx = (np.abs(array_radii_intended - 0.05 - self.radius)).argmin()
        self._radius_intended = array_radii_intended[idx]




