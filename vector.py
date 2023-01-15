import math
import decimal
from decimal import Decimal, getcontext
import numpy as np

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.multiply_scalar(Decimal('1.0')/Decimal(magnitude))

        except ZeroDivisionError:
            raise Expectaion('Cannot normalize the zero vector')

    def plus(self, v):
        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #     new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]

        return Vector(new_coordinates)
    
    def minus(self, v):
        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #     new_coordinates.append(self.coordinates[i] - v.coordinates[i])
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def multiply_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def vector_from_coordinates():
        x1 = int(input("type value of x1: "))
        x2 = int(input("type value of x2: "))
        y1 = int(input("type value of y1: "))
        y2 = int(input("type value of y2: "))
        z1 = int(input("type value of z1: "))
        z2 = int(input("type value of z2: "))
        vector_value = tuple([x2-x1, y2-y1, z2 -z1])
        return vector_value

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or 
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == math.pi )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def cross(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        new_coordinates = [ 
        y1*z2 - y2*z1, 
        -(x1*z2 - x2*z1),
        x1*y2 - x2*y1 ]

        return Vector(new_coordinates)
        
    def angle_with(self, v, in_degrees=False):
        try:
            # unit_vector1 = self.normalize()
            # unit_vector2 = v.normalize()
            angle_in_radians = math.acos(self.dot(v) / Decimal(self.magnitude()*v.magnitude()))

            if in_degrees:
                degrees_per_radian = 180 / math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def __str__(self):
        coordinates_as_floats = map(float, self.coordinates)
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates





# vector1 = Vector([8.218, -9.341])
# vector2 = Vector([-1.129, 2.111])
# print('operation 1: ',vector1.plus(vector2))

# vector3 = Vector([7.119, 8.215])
# vector4 = Vector([-8.223, 0.878])
# print('operation 2: ', vector3.minus(vector4))

# vector5 = Vector([1.671, -1.012, -0.318])
# scalar = 7.41
# print('operation 3: ', vector5.multiply_scalar(scalar))

v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
# print('The dot product =',v.dot(w))

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
# print('The dot product =',v.dot(w))

# v = Vector([3.183, -7.627])
# w = Vector([-2.668, 5.319])
# print('The angle equals =', v.angle_with(w),'rad')

# v = Vector([7.35, 0.221, 5.188])
# w = Vector([2.751, 8.259, 3.985])
# print('The angle equals =', v.angle_with(w, in_degrees=True),'d')


# DID NOT SOLVE THE PROBLEM WITH DOT PRODUCT IN (is_parallel_to) METHOD
# v = Vector(['-7.579', '-7.88'])
# w = Vector(['22.737', '23.64'])
# # print('is parallel:', v.is_parallel_to(w))
# # print('is orthogonal:', v.is_orthogonal_to(w))
# # x = v.normalize()
# # y = w.normalize()
# print('see',v.dot(w))

v = Vector(['8.461', '7.893', '-8.187'])
w = Vector(['6.984', '-5.975', '4.778'])
# print('the cross product is:', v.cross(w))

v = Vector(['-2', '0', '3'])
u = Vector(['1', '5', '2'])
print(u.minus(v))