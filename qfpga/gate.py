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
    q = QVector(*[inputs[i] for i in range(inputs.size)])
    q = self.matrix_(q)
    for i in range(inputs.size):
      inputs[i] = q[0][i][0]
    # if isinstance(inputs, list):
    #   q = Qubit(n=len(inputs)*2)
    #   for i, x in enumerate(inputs):
    #     q[2*i] = x[0]
    #     q[2*i + 1] = x[1]
    # else:
    #   q = inputs
    # return q.transform(self.matrix_)

    # if isinstance(inputs, list):
    #   q = [0 for _ in range(len(inputs) * 2)]
    #   for i, x in enumerate(inputs):
    #     q[2*i] = x[0]
    #     q[2*i + 1] = x[1]
    #   q = QVector(*q)
    #   q = self.matrix_(q)
    #   for i, x in enumerate(inputs):
    #     x[0] = q[0][2*i][0]
    #     x[1] = q[0][2*i + 1][0]
    # else:
    #   q = QVector(inputs[0], inputs[1])
    #   q = self.matrix_(q)
    #   inputs[0], inputs[1] = q[0][0][0], q[0][1][0]
    # return inputs

    # return self.matrix_(q)
