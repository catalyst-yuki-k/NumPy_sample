# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes

# NumPyをインポートする
import numpy as np

x = np.array([[0, 1], [2, 3]], dtype='<u2')
print(x.tobytes())
# b'\x00\x00\x01\x00\x02\x00\x03\x00'
print(x.tobytes('C') == x.tobytes())
# True
print(x.tobytes('F'))
# b'\x00\x00\x02\x00\x01\x00\x03\x00'