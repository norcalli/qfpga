class Circuit(Gate):
  def __init__(self, name, gates):
    self.name = name
    self.gates = gates

  def run(self, **input):
    """
    Provided a mapping of names to inputs.
    Returns a list of corresponding names to outputs.
    """
    return []
