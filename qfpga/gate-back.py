class Gate():
<<<<<<< HEAD
  type_map = {'CNOT': Gate.CNOT, 'H': Gate.Hadamard}

  def __init__(self, type, args, inputs):
    self.type = type

  def CNOT(args, inputs):
    pass

  def Hadamard(args, inputs):
    pass
=======
  def __init__(self, name, matrix, args):
    self.name = name
    self.matrix_ = matrix

  def transform(input):
    return input
>>>>>>> 277c17e1ff38d581a084905190636dc01591886a
