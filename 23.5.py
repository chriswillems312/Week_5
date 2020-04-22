import numpy as np

def add_vector(vector1, vector2) :
    print(np.add([vector1], [vector2]))
add_vector([1, 2], [2, 3])

def scalar_mult(scalar, vector2) :
    a = np.array(vector2)
    print(scalar * a)
scalar_mult([1], [2, 3])

def dot_product(vec1, vec2):
    print(np.dot(vec1, vec2))

dot_product([1, 2], [1, 4])

def cross_product(vec1, vec2) :
    print(np.cross(vec1, vec2))
cross_product([1, 1], [1, 4])