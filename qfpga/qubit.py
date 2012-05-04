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
    return self

  def measure(self, rand = random.random):
    probabilities = [self.probability(i) for i in range(self.size)]
    return weighted_choice(probabilities)

class Variable:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __repr__(self):
    return str(self)

  def __mul__(self, other):
    return Variable('{} * {}'.format(self, other))

  def __div__(self, other):
    return Variable('{} / {}'.format(self, other))

  def __add__(self, other):
    return Variable('( {} + {} )'.format(self, other))

  def __sub__(self, other):
    return Variable('( {} - {} )'.format(self, other))
    
  def __neg__(self):
    return Variable('- {}'.format(self))

class Vector:
  def __init__(self, n):
    if isinstance(n, list):
      self.data = n
    elif isinstance(n, int):
      self.data = [0 for _ in range(n)]
    else:
      raise ValueError('{} is not a valid argument for Vector'.format(type(n)))

  def __iter__(self):
    for x in self.data:
      yield x

  def __getitem__(self, i):
    return self.data[i]

  def __setitem__(self, i, v):
    self.data[i] = v

class Matrix:
  def __init__(self, m, n = None):
    if n is None:
      # For initialization as: Matrix([[1, 2], [3, 4]])
      if isinstance(m[0], list):
        self.size = (len(m), len(m[0]))
        self.matrix = m
      # For initialization as: Matrix([Vector(1, 2), Vector(3, 4)])
      elif isinstance(m[0], Vector):
        self.size = (len(m[0]), len(m))
        self.matrix = [[m[i][k] for i in range(self.size[1])] for k in range(self.size[0])]
      # For a 1x1 matrix: Matrix([1])
      elif isinstance(m[0], int):
        self.size = (1, 1)
        self.matrix = [[m[0]]]
      else:
        raise ValueError('{} is not a valid argument for Matrix().'.format(type(m)))
    else:
    # self.size = (m, n)
      self.size = (m, n)
      self.matrix = [[0 for _ in range(n)] for _ in range(m)]

  def __iter__(self):
    for row in self.matrix:
      yield row
      
  def __call__(self, i, j, v = None):
    if v is None:
      return self.matrix[i][j]
    else:
      self.matrix[i][j] = v

  def __mul__(self, o):
    return Matrix([[elem * o for elem in row] for row in self])

  def __getitem__(self, i):
    return self.matrix[i]

  def __str__(self):
    return str(self.matrix)

  def __repr__(self):
    return str(self)

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
  

