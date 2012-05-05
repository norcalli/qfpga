# from qmatrix import QMatrix as Matrix
from matrix import Matrix, Vector
import math

i = complex(0,1)

# Technically Hadamard is a special case of rotation.
H = Matrix([[1, 1],
            [1, -1]]) * (0.5 ** 0.5)

X = Matrix([[0, 1],
            [1, 0]])
Y = Matrix([[0, -i],
            [i, 0]])
Z = Matrix([[1, 0],
            [0, -1]])

# I = Matrix([0, 1], [1, 0])
I = Matrix([[1, 0],
            [0, 1]])

CNOT = Matrix([[1,0,0,0],
               [0,1,0,0],
               [0,0,0,1],
               [0,0,1,0]])

def rotX(theta):
  return I * math.cos(theta/2) + X * i * math.sin(theta/2)

def rotY(theta):
  return I * math.cos(theta/2) + Y * i * math.sin(theta/2)

def rotZ(theta):
  return I * math.cos(theta/2) + Z * i * math.sin(theta/2)
