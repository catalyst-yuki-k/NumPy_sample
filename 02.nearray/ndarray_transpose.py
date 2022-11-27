# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose

# NumPyをインポートする
import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
# [[1 2]
#  [3 4]]
print(a.transpose())
# [[1 3]
#  [2 4]]
print(a.transpose((1, 0)))
# [[1 3]
#  [2 4]]
print(a.transpose(1, 0))
# [[1 3]
#  [2 4]]