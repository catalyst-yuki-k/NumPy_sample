# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view

# NumPyをインポートする
import numpy as np

x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])

# Viewing array data using a different type and dtype:

y = x.view(dtype=np.int16, type=np.matrix)
print(y)
# [[513]]
print(type(y))
# <class 'numpy.matrix'>

# Creating a view on a structured array so it can be used in calculations

x = np.array([(1, 2),(3,4)], dtype=[('a', np.int8), ('b', np.int8)])
xv = x.view(dtype=np.int8).reshape(-1,2)
print(xv)
# [[1 2]
#  [3 4]]
print(xv.mean(0))
# [2. 3.]

# Making changes to the view changes the underlying array

xv[0,1] = 20
print(x)
# [(1, 20) (3,  4)]

# Using a view to convert an array to a recarray:

z = x.view(np.recarray)
print(z.a)
# [1 3]

# Views share data:

x[0] = (9, 10)
print(z[0])
# (9, 10)

# Views that change the dtype size (bytes per entry) should normally be avoided on arrays defined by slices, transposes, fortran-ordering, etc.:

x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int16)
y = x[:, ::2]
print(y)
# [[1 3]
#  [4 6]]
print(y.view(dtype=[('width', np.int16), ('length', np.int16)]))
# Traceback (most recent call last):
#   File "c:\github\repository\NumPy_sample\02.nearray\ndarray_view.py", line 51, in <module>
#     print(y.view(dtype=[('width', np.int16), ('length', np.int16)]))
# ValueError: To change to a dtype of a different size, the last axis must be contiguous
z = y.copy()
print(z.view(dtype=[('width', np.int16), ('length', np.int16)]))
# [[(1, 3)]
#  [(4, 6)]]

# However, views that change dtype are totally fine for arrays with a contiguous last axis, even if the rest of the axes are not C-contiguous:

x = np.arange(2 * 3 * 4, dtype=np.int8).reshape(2, 3, 4)
print(x.transpose(1, 0, 2).view(np.int16))
# [[[ 256  770]
#   [3340 3854]]
#
#  [[1284 1798]
#   [4368 4882]]
#
#  [[2312 2826]
#   [5396 5910]]]