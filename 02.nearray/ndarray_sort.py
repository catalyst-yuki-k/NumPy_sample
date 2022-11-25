# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort

# NumPyをインポートする
import numpy as np

a = np.array([[1,4], [3,1]])
a.sort(axis=1)
print(a)
# [[1 4]
#  [1 3]]

a.sort(axis=0)
print(a)
# [[1 3]
#  [1 4]]

#Use the order keyword to specify a field to use when sorting a structured array:
a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
a.sort(order='y')
print(a)
# [(b'c', 1) (b'a', 2)]