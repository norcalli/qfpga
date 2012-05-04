import math
import test
import random
import random

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
  

class Qubit():
  count = 0

  # def __init__(self, name, n = 2):
  def __init__(self, name = None, n = 2, state = None):
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

  def __str__(self):
    return '{} = {}'.format(self.name, self.state)

  def __repr__(self):
    return '{} = {}'.format(self.name, self.state)

  def transform(self, m):
    # assert(m.length == self.size)
    assert(m.size[0] == self.size)
    for i in range(self.size):
      self[i] = sum(m[i][k] * self[k] for k in range(self.size))
    return self

  def measure(self, rand = random.random):
    probabilities = [self.probability(i) for i in range(self.size)]
    return weighted_choice(probabilities)

def cache(fn):
  result = None
  def new(*args):
    nonlocal result
    if result is None:
      result = fn(*args)
    return result
  return new

def cache(fn):
  cached, result = False, None
  def new(*args):
    nonlocal result, cached
    if not cached:
      cached, result = True, fn(*args)
    return result
  return new

@cache
def LargeCalc():
  print(''.join('0' for i in range(100)))

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
  

