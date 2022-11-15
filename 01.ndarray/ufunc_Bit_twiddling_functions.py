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
# [26  6]
print(np.bitwise_xor([31,3], [5,6]))
# [26  5]
print(np.bitwise_xor([True, True], [False, True]))
# [ True False]
# The ^ operator can be used as a shorthand for np.bitwise_xor on ndarrays.
x1 = np.array([True, True])
x2 = np.array([False, True])
print(x1 ^ x2)
# [ True False]


# invert(x, /[, out, where, casting, order, ...])
# Compute bit-wise inversion, or bit-wise NOT, element-wise.
# We’ve seen that 13 is represented by 00001101. The invert or bit-wise NOT of 13 is then:
x = np.invert(np.array(13, dtype=np.uint8))
print(x)
# 242
print(np.binary_repr(x, width=8))
# 11110010
#The result depends on the bit-width:
x = np.invert(np.array(13, dtype=np.uint16))
print(x)
# 65522
print(np.binary_repr(x, width=16))
# 1111111111110010
# When using signed integer types the result is the two’s complement of the result for the unsigned type:
print(np.invert(np.array([13], dtype=np.int8)))
# [-14]
print(np.binary_repr(-14, width=8))
# 11110010
# Booleans are accepted as well:
print(np.invert(np.array([True, False])))
# [False  True]
# The ~ operator can be used as a shorthand for np.invert on ndarrays.
x1 = np.array([True, False])
print(~x1)
# [False  True]


# left_shift(x1, x2, /[, out, where, casting, ...])
# Shift the bits of an integer to the left.
print(np.binary_repr(5))
# 101
print(np.left_shift(5, 2))
# 20
print(np.binary_repr(20))
# 10100
print(np.left_shift(5, [1,2,3]))
# [10 20 40]
# Note that the dtype of the second argument may change the dtype of the result and can lead to unexpected results in some cases (see Casting Rules):
a = np.left_shift(np.uint8(255), 1) # Expect 254
print(a, type(a)) # Unexpected result due to upcasting
# 510 <class 'numpy.intc'>
b = np.left_shift(np.uint8(255), np.uint8(1))
print(b, type(b))
# 254 <class 'numpy.uint8'>
# The << operator can be used as a shorthand for np.left_shift on ndarrays.
x1 = 5
x2 = np.array([1, 2, 3])
print(x1 << x2)
# [10 20 40]


# right_shift(x1, x2, /[, out, where, ...])
# Shift the bits of an integer to the right.
print(np.binary_repr(10))
# 1010
print(np.right_shift(10, 1))
# 5
print(np.binary_repr(5))
# 101
print(np.right_shift(10, [1,2,3]))
# [5 2 1]
# The >> operator can be used as a shorthand for np.right_shift on ndarrays.
x1 = 10
x2 = np.array([1,2,3])
print(x1 >> x2)
# [5 2 1]