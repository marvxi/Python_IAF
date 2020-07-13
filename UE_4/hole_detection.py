"""
Module description
@date: June 2020
@author: Hendrik Traub <h.traub@tu-bs.de>
@Copyright: 2020 TU Braunschweig
<www.tu-braunschweig.de>. All rights reserved.
"""
from holes import HoleDetection

filename = '\holes.JPG'
filepath = r"C:\Users\Marvi\Documents\Pycharm_Projects\Python_IAF\UE_4"
hole_detection = HoleDetection(filename=filename, filepath=filepath)
hole_detection.Image
hole_detection.holeList
hole_detection.plotRadii()

