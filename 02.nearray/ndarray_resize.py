# NumPyをインポートする
import numpy as np

# Shrinking an array: array is flattened (in the order that the data are stored in memory), resized, and reshaped:

a = np.array([[0, 1], [2, 3]], order='C')
a.resize((2, 1))
print(a)
# [[0]
#  [1]]
a = np.array([[0, 1], [2, 3]], order='F')
a.resize((2, 1))
print(a)
# [[0]
#  [2]]
# Enlarging an array: as above, but missing entries are filled with zeros:

b = np.array([[0, 1], [2, 3]])
b.resize(2, 3) # new_shape parameter doesn't have to be a tuple
print(b)
# [[0 1 2]
#  [3 0 0]]
# Referencing an array prevents resizing…

c = a
a.resize((1, 1))
# Traceback (most recent call last):
# ...
# ValueError: cannot resize an array that references or is referenced ...
# Unless refcheck is False:

a.resize((1, 1), refcheck=False)
print(a)
# [[0]]
print(c)
# [[0]]