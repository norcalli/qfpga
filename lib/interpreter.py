import re

def createGate(str):
  m = re.search('^(\w+)\((.*?)\) (.+)$', str)
  gate, args, inputs = m.group(1), m.group(2).split(','), m.group(3).split(',')
  return Gate(gate, args, inputs)

# First line should be the name of the circuit (so that subcircuits can be used).

# Other lines should look like "GATE(arg1,arg2) input1,input2,etc".
# Args may be unused.
def interpret(buf):
  lines = '\n'.split(buf)
  gates = map(createGate, lines[1::])
  return Circuit(lines[0], gates)
