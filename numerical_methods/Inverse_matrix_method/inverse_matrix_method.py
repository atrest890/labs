#!/usr/bin/env python3

import numpy as np

mx_a = np.array([[1, 1, 0], 
                [1, 2, 1], 
                [0, 1, 2]])

mx_b = np.array([2, 4, 3])
print(mx_a)
print(mx_b)
inv_mx_a = np.linalg.inv(mx_a)
print("Inverse matrix:")
print(inv_mx_a)
print("X-Matrix:")
print(np.dot(inv_mx_a, mx_b))

