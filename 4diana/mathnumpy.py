import math
import numpy
sevfiv = 75
ninty = 90
oneheghty = 180

def deg2rad(a):
    print('Матн: ',math.radians(a))
    print('Numpy: ',numpy.radians(a))
    print(math.radians(a) == numpy.radians(a))
deg2rad(sevfiv)
deg2rad(ninty)
deg2rad(oneheghty)
