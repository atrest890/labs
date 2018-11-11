import numpy as np
import copy

mx_a = np.array([[1, 1, 0], [1, 2, 1], [0, 1, 2]])
mx_b = np.array([2, 4, 3])
detX = np.linalg.det(mx_a)
print("Solution of the equation:")
for i in range(3):
    mx_i = copy.copy(mx_a)
    mx_i[:,i] = mx_b
    detXi = np.linalg.det(mx_i)
    r = detXi / detX
    print(r)
