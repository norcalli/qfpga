from qubit import Qubit
from qmatrix import *

class Gate():
  # type_map = {'CNOT': Gate.CNOT, 'H': Gate.Hadamard}

  # def __init__(self, name, matrix, args, inputs):
  #   self.type = type

  # def CNOT(args, inputs):
  #   pass

  # def Hadamard(args, inputs):
  #   pass

  def __init__(self, name, matrix, args):
    self.name = name
    self.matrix_ = matrix

  def transform(self, inputs):
    # if isinstance(inputs, list):
    #   q = Qubit(n=len(inputs)*2)
    #   for i, x in enumerate(inputs):
    #     q[2*i] = x[0]
    #     q[2*i + 1] = x[1]
    # else:
    #   q = inputs
    # return q.transform(self.matrix_)
    if isinstance(inputs, list):
      q = [0 for _ in range(len(inputs) * 2)]
      for i, x in enumerate(inputs):
        q[2*i] = x[0]
        q[2*i + 1] = x[1]
      q = QVector(*q)
    else:
      q = QVector(inputs[0], inputs[1])
    return self.matrix_(q)
