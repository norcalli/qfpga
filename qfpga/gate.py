class Gate():
  type_map = {'CNOT': Gate.CNOT, 'H': Gate.Hadamard}

  def __init__(self, type, args, inputs):
    self.type = type

  def CNOT(args, inputs):
    pass

  def Hadamard(args, inputs):
    pass
