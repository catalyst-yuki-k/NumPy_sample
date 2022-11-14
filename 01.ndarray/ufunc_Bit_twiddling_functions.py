import numpy as np

# bitwise_and(x1, x2, /[, out, where, ...])
# Compute the bit-wise AND of two arrays element-wise.
# The number 13 is represented by 00001101. Likewise, 17 is represented by 00010001. 
# The bit-wise AND of 13 and 17 is therefore 000000001, or 1:
print(np.bitwise_and(13, 17))
# 1
print(np.bitwise_and(14, 13))
# 12
print(np.binary_repr(12))
# 1100
print(np.bitwise_and([14,3], 13))
# [12  1]
print(np.bitwise_and([11,7], [4,25]))
# [0 1]
print(np.bitwise_and(np.array([2,5,255]), np.array([3,14,16])))
# [ 2  4 16]
print(np.bitwise_and([True, True], [False, True]))
# [False  True]
# The & operator can be used as a shorthand for np.bitwise_and on ndarrays.
x1 = np.array([2, 5, 255])
x2 = np.array([3, 14, 16])
print(x1 & x2)
# [ 2  4 16]


# bitwise_or(x1, x2, /[, out, where, casting, ...])
# Compute the bit-wise OR of two arrays element-wise.
# The number 13 has the binary representation 00001101. Likewise, 16 is represented by 00010000. 
# The bit-wise OR of 13 and 16 is then 000111011, or 29:
print(np.bitwise_or(13, 16))
# 29
print(np.binary_repr(29))
# 11101
print(np.bitwise_or(32, 2))
# 34
print(np.bitwise_or([33, 4], 1))
# [33  5]
print(np.bitwise_or([33, 4], [1, 2]))
# [33  6]
print(np.bitwise_or(np.array([2, 5, 255]), np.array([4, 4, 4])))
# [  6   5 255]
print(np.array([2, 5, 255]) | np.array([4, 4, 4]))
# [  6   5 255]
print(np.bitwise_or(np.array([2, 5, 255, 2147483647], dtype=np.int32), np.array([4, 4, 4, 2147483647], dtype=np.int32)))
# [         6          5        255 2147483647]
print(np.bitwise_or([True, True], [False, True]))
# [ True  True]
# The | operator can be used as a shorthand for np.bitwise_or on ndarrays.
x1 = np.array([2, 5, 255])
x2 = np.array([4, 4, 4])
print(x1 | x2)
# [  6   5 255]


# bitwise_xor(x1, x2, /[, out, where, ...])
# Compute the bit-wise XOR of two arrays element-wise.
# The number 13 is represented by 00001101. Likewise, 17 is represented by 00010001. 
# The bit-wise XOR of 13 and 17 is therefore 00011100, or 28:
print(np.bitwise_xor(13, 17))
# 28
print(np.binary_repr(28))
# 11100
print(np.bitwise_xor(31, 5))
# 26
print(np.bitwise_xor([31,3], 5))
# array([26,  6])
print(np.bitwise_xor([31,3], [5,6]))
# array([26,  5])
print(np.bitwise_xor([True, True], [False, True]))
# array([ True, False])
# The ^ operator can be used as a shorthand for np.bitwise_xor on ndarrays.
x1 = np.array([True, True])
x2 = np.array([False, True])
print(x1 ^ x2)
# array([ True, False])


# invert(x, /[, out, where, casting, order, ...])
# Compute bit-wise inversion, or bit-wise NOT, element-wise.


# left_shift(x1, x2, /[, out, where, casting, ...])
# Shift the bits of an integer to the left.


# right_shift(x1, x2, /[, out, where, ...])
# Shift the bits of an integer to the right.
