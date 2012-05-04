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


class QubitSystem:
  def __init__(self, qubits):
    self.qubits = qubits

  def isEntangled():
    pass

n = 2
qubits = [Qubit() for _ in range(n)]
system_state = generateSystem(qubits)


print(qubits, '=', system_state)

qubits[0].transform(H)
system_state = generateSystem(qubits)
print(qubits, '=', system_state)

system_state.transform(CNOT)
print(qubits, '=', system_state)


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
