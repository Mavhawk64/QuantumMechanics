import numpy as np


def pauli_x():
    return np.array([[0, 1], [1, 0]])


def pauli_y():
    return np.array([[0, -1j], [1j, 0]])


def pauli_z():
    return np.array([[1, 0], [0, -1]])


def identity():
    return np.array([[1, 0], [0, 1]])


# xyy, yxy, yyx
xyy = np.matmul(pauli_x(), np.matmul(pauli_y(), pauli_y())).real
yxy = np.matmul(pauli_y(), np.matmul(pauli_x(), pauli_y())).real
yyx = np.matmul(pauli_y(), np.matmul(pauli_y(), pauli_x())).real

print(xyy)
print(yxy)
print(yyx)
