class Matrix():
  def __init__(self, *m):
    # Remember: vectors are matrices.
    self.matrix_ = m

  def __iter__(self):
    for i in range(len(self.matrix_)):
      yield i

  def __getitem__(self, i):
    return self.matrix_[i]

  def __len__(self):
    return len(self.matrix_)

  def __call__(self, mat):
    # mat is m*j, self.matrix_ is i*m.
    return Matrix([[sum(self[i][j] * mat[j][m]
                        for j in self)
                    for m in range(len(mat[0]))]
                   for i in self])

  def __mul__(self, scalar):
    return Matrix(*[[self[i][j] * scalar for j in range(len(self[i]))]
                    for i in self])
"""
Examples:

m = Matrix([1, 1 ],
           [1, -1])
v = Matrix([1 ],
           [-1])
H = Matrix([1, 1 ],
           [1, -1])
           * (0.5 ** 0.5))

"""
