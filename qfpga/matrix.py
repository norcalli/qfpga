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
