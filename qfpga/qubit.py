import math
import test
import random
import math

def weighted_choice(weights):
  totals = []
  running_total = 0

  for w in weights:
    running_total += w
    totals.append(running_total)
    
  rnd = random.random() * running_total
  for i, total in enumerate(totals):
    if rnd < total:
      return i

def magnitude(vector):
  return math.sqrt(sum(abs(x)**2 for x in vector))
  
def bits(i,n):
  return tuple((0,1)[i>>j & 1] for j in range(n-1,-1,-1))

def tensorIndices(n):
  for i in range(2**n):
    yield bits(i, n)

# def sum(x):
#   x = list(x)
#   total = x[0]
#   for i in x[1:]:
#     total = total + i
#   return total

class Qubit():
  count = 0

  # def __init__(self, name, n = 2):
  def __init__(self, name = None, n = 2, state = None, system = None):
    self.system = system
    if name is None:
      self.name_ = 'q' + str(Qubit.count)
      Qubit.count += 1
    else:
      self.name_ = name
    # self.name = name
    if state is None:
      self.state = [0 for _ in range(n)]
      self.state[0] = 1
    else:
      self.state = state
    self.size_ = n;

  # def magnitude(self):
  #   return math.sqrt(sum([abs(x)**2 for x in self.state]))
  
  # def __abs__(self):
  #   return self.magnitude()

  def validState(self):
    if magnitude(self.state) != 1:
      return False

  def normalize(self):
    m = magnitude(self.state)
    assert(m != 0)
    self.state = [x / m for x in self.state]
    return self

  @property
  def size(self):
    return self.size_

  @property
  def name(self):
    return self.name_

  def __getitem__(self, i):
    return self.state[i]

  def __setitem__(self, i, value):
    self.state[i] = value
    # self.normalize()

  def probability(self, i):
    return abs(self[i])**2

  def __iter__(self):
    for x in self.state:
      yield x

  def __len__(self):
    return self.size

  def __str__(self):
    k = round(math.log(self.size, 2))
    return ' + '.join('{} |{}>'.format(self[i], ''.join(str(_) for _ in indices)) for i, indices in enumerate(tensorIndices(k)) if self[i])
    # return '{} = {}'.format(self.name, self.state)

  def __repr__(self):
    return str(self)

  def transform(self, m):
    # assert(m.length == self.size)
    assert m.size[1] == self.size, "m.size = {}; self.size = {}".format(m.size, self.size)
    # self.state = [sum(m[i][k] * self[k] for k in range(self.size)) for i in range(self.size)]
    self.state = [sum(a * v for a, v in zip(row, self)) for row in m]
    # for i in range(self.size):
    #   self[i] = sum(m[i][k] * self[k] for k in range(self.size))
      # self[i] = sum(a * v for a, v in zip(m[i], self))
    if self.system:
      self.system.update()
    return self

  def measure(self, rand = random.random):
    probabilities = [self.probability(i) for i in range(self.size)]
    return weighted_choice(probabilities)

@test.main
def doit(*args):
  psi = Qubit(n = 2)
  print(psi)
  psi[0] = 1j
  psi[1] = 5 + 3j
  print(psi)
  identity = [ [2*int(i == j) for i in range(psi.size)] for j in range(psi.size)]
  print(identity)
  print(psi.transform(identity).normalize())
  # print(abs(psi))
  

