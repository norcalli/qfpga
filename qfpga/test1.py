from qmatrix import *
from univ_gates import *
from qubit import *
from gate import *
import random

HGate = Gate('Hadamard', H, None)
CNOTGate = Gate('CNOT', CNOT, None)


q = Qubit()
qs = [Qubit() for _ in range(2)]

for x in qs:
  x[0] = random.random() + i * random.random()
  x[1] = random.random() + i * random.random()
  x.normalize()

print(HGate.transform(q))
print(CNOTGate.transform(qs))


v = QVector(1, 0)

print(I)
print()

print(I(v))
print()

print(H(v))
print()

print(Z(v))
print()
