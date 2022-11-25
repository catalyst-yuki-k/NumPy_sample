# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags

# NumPyをインポートする
import numpy as np

y = np.array([[3, 1, 7],
              [2, 0, 0],
              [8, 5, 9]])
print(y)
# [[3, 1, 7],
#  [2, 0, 0],
#  [8, 5, 9]])

print(y.flags)
#  C_CONTIGUOUS : True
#  F_CONTIGUOUS : False
#  OWNDATA : True
#  WRITEABLE : True
#  ALIGNED : True
#  WRITEBACKIFCOPY : False

y.setflags(write=0, align=0)
print(y.flags)
#  C_CONTIGUOUS : True
#  F_CONTIGUOUS : False
#  OWNDATA : True
#  WRITEABLE : False
#  ALIGNED : False
#  WRITEBACKIFCOPY : False

print(y.setflags(uic=1))
# Traceback (most recent call last):
#   File "ndarray_setflags.py", line 29, in <module>
#     print(y.setflags(uic=1))
# ValueError: cannot set WRITEBACKIFCOPY flag to True