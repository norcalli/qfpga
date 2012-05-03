from qfpga import matrix, gate

# Technically Hadamard is a special case of rotation.
H = Matrix([1, 1 ], [1, -1]) * (0.5 ** 0.5)

