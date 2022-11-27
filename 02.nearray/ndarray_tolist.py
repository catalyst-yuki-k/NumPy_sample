# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist

# NumPyをインポートする
import numpy as np

a = np.uint32([1, 2])
a_list = list(a)
print(a_list)
# [1, 2]
print(type(a_list[0]))
# <class 'numpy.uint32'>
a_tolist = a.tolist()
print(a_tolist)
# [1, 2]
print(type(a_tolist[0]))
# <class 'int'>

# Additionally, for a 2D array, tolist applies recursively:

a = np.array([[1, 2], [3, 4]])
print(list(a))
# [array([1, 2]), array([3, 4])]
print(a.tolist())
# [[1, 2], [3, 4]]

#The base case for this recursion is a 0D array:

a = np.array(1)
print(list(a))
# Traceback (most recent call last):
#   File "c:\github\repository\NumPy_sample\02.nearray\ndarray_tolist.py", line 29, in <module>
#     print(list(a))
# TypeError: iteration over a 0-d array
print(a.tolist())
# 1