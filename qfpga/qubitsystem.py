from functools import reduce
from qmatrix import *
from univ_gates import *
from gate import *
from qubit import *
import math
import random

HGate = Gate('Hadamard', H, None)
CNOTGate = Gate('CNOT', CNOT, None)

def bits(i,n):
  return tuple((0,1)[i>>j & 1] for j in xrange(n-1,-1,-1))

def bits(i,n):
  return tuple((0,1)[i>>j & 1] for j in range(n-1,-1,-1))

def tensorIndices(n):
  for i in range(2**n):
    yield bits(i, n)


def generateSystem(qubits):
  n = len(qubits)
  system_state = Qubit(n=2**n)
  for i, indices in enumerate(tensorIndices(n)):
    value = reduce(lambda x, y: x*y, [qubits[j][k] for j, k in enumerate(indices)])
    system_state[i] = value
  return system_state


def qtos(q):
  k = round(math.log(q.size, 2))
  return ' + '.join('{} |{}>'.format(q[i], ''.join(str(_) for _ in indices)) for i, indices in enumerate(tensorIndices(k)) if q[i])


# m = 2
# vtest = Vector([Variable('v{}'.format(i)) for i in range(m)])
# mtest = Matrix([ [Variable('a{}{}'.format(j, i)) for i in range(m)] for j in range(m)])
# qtest = Qubit(n=m)
# for i in range(m):
#   qtest[i] = Variable('q{}'.format(i))

# print(qtest)
# print(mtest)
# print(qtest.transform(mtest))


def only(x, allof):
  noneof = set(range(len(x))) - set(allof)
  return all(x[i] for i in allof) and not any(x[i] for i in noneof)

class EntangledException(Exception):
  def __init__(self):
    Exception.__init__(self, "The system is entangled, can't extract qubit")

# TODO: Add a reference to QubitSystem for Qubit so that when a Qubit is update, it
# automatically updates the system.
class QubitSystem:
  def __init__(self, qubits):
    self.qubits = qubits
    self.size = len(qubits)
    self.state = Qubit(n=2**self.size)
    self.generateSystem(qubits)
    for qubit in qubits:
      qubit.system = self
    self.is_entangled = False

  @property
  def entangled(self):
    if self.is_entangled is not None:
      return self.is_entangled
    if self.size == 1:
      return False
    self.is_entangled = only(self.state, [0, self.state.size - 1]) or only(self.state, [2**i for i in range(self.size)])
    return self.is_entangled
    
  def generateSystem(self, qubits = None):
    if qubits is None:
      qubits = self.qubits
    for i, indices in enumerate(tensorIndices(n)):
      self.state[i] = reduce(lambda x, y: x*y, [qubits[j][k] for j, k in enumerate(indices)])
    return self.state

  def update(self):
    self.generateSystem()
    self.is_entangled = None

  def transform(self, m):
    self.state.transform(m)
    self.is_entangled = None
    if not self.entangled:
      self.generateSystem()

  def __iter__(self):
    pass

  def __getitem__(self, i):
    if self.entangled:
      # return self.state[i]
      raise EntangledException()
    return self.qubits[i]

  def __str__(self):
    return str(self.state)

  def __repr__(self):
    return str(self)

n = 2
qubits = [Qubit() for _ in range(n)]
system_state = generateSystem(qubits)

system = QubitSystem(qubits)

print(' (x) '.join(str(qubit) for qubit in qubits), '=', system)

system[0].transform(H)

system.transform(CNOT)
print('SYSTEM:', system, '; isEntangled = ', system.entangled)

system.transform(CNOT)
print('SYSTEM:', system, '; isEntangled = ', system.entangled)

# qubits[0].transform(H)
# print('SYSTEM:', system, '; isEntangled = ', system.entangled)

# HGate.transform(qubits[0])
# system_state = generateSystem(qubits)
# print(qubits, '=', generateSystem(qubits))
# CNOTGate.transform(system_state)
# print(qubits, '=', system_state)

print(qubits[0])

for i, indices in enumerate(tensorIndices(n)):
  value = reduce(lambda x, y: x*y, [qubits[j][k] for j, k in enumerate(indices)])
  system_state[i] = value

print(system_state)

# class QubitSystem:
#   def __init__(self):
#     Qubit(
print([x for x in tensorIndices(3)])
