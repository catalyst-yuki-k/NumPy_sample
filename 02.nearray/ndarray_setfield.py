# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setfield.html#numpy.ndarray.setfield

# NumPyをインポートする
import numpy as np

x = np.eye(3)
print(x.getfield(np.float64))
# [[1.,  0.,  0.],
#  [0.,  1.,  0.],
#  [0.,  0.,  1.]])

x.setfield(3, np.int32)
print(x.getfield(np.int32))
# [[3, 3, 3],
#  [3, 3, 3],
#  [3, 3, 3]], dtype=int32)

print(x)
# [[1.0e+000, 1.5e-323, 1.5e-323],
#  [1.5e-323, 1.0e+000, 1.5e-323],
#  [1.5e-323, 1.5e-323, 1.0e+000]])

x.setfield(np.eye(3), np.int32)
print(x)
# [[1.,  0.,  0.],
#  [0.,  1.,  0.],
#  [0.,  0.,  1.]])