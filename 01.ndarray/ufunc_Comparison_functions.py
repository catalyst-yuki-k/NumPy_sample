import numpy as np

# greater(x1, x2, /[, out, where, casting, ...])
# Return the truth value of (x1 > x2) element-wise.
print(np.greater([4,2],[2,2]))
# [ True False]
# The > operator can be used as a shorthand for np.greater on ndarrays.
a = np.array([4, 2])
b = np.array([2, 2])
print(a > b)
# [ True False]


# greater_equal(x1, x2, /[, out, where, ...])
# Return the truth value of (x1 >= x2) element-wise.
print(np.greater_equal([4, 2, 1], [2, 2, 2]))
# [ True True False]
# The >= operator can be used as a shorthand for np.greater_equal on ndarrays.
a = np.array([4, 2, 1])
b = np.array([2, 2, 2])
print(a >= b)
# [ True  True False]


# less(x1, x2, /[, out, where, casting, ...])
# Return the truth value of (x1 < x2) element-wise.
print(np.less([1, 2], [2, 2]))
# [ True False])
# The < operator can be used as a shorthand for np.less on ndarrays.
a = np.array([1, 2])
b = np.array([2, 2])
print(a < b)
# [ True False]


# less_equal(x1, x2, /[, out, where, casting, ...])
# Return the truth value of (x1 <= x2) element-wise.
print(np.less_equal([4, 2, 1], [2, 2, 2]))
# [False  True  True]
# The <= operator can be used as a shorthand for np.less_equal on ndarrays.
a = np.array([4, 2, 1])
b = np.array([2, 2, 2])
print(a <= b)
# [False  True  True]


# not_equal(x1, x2, /[, out, where, casting, ...])
# Return (x1 != x2) element-wise.
print(np.not_equal([1.,2.], [1., 3.]))
# [False,  True]
print(np.not_equal([1, 2], [[1, 3],[1, 4]]))
# [[False  True]
#  [False  True]]
# The != operator can be used as a shorthand for np.not_equal on ndarrays.
a = np.array([1., 2.])
b = np.array([1., 3.])
print(a != b)
# [False,  True]


# equal(x1, x2, /[, out, where, casting, ...])
# Return (x1 == x2) element-wise.
print(np.equal([0, 1, 3], np.arange(3)))
# [ True  True False]
# What is compared are values, not types. So an int (1) and an array of length one can evaluate as True:
print(np.equal(1, np.ones(1)))
# [ True]
# The == operator can be used as a shorthand for np.equal on ndarrays.
a = np.array([2, 4, 6])
b = np.array([2, 4, 2])
print(a == b)
# [ True  True False]


# Warning
# Do not use the Python keywords and and or to combine logical array expressions. 
# These keywords will test the truth value of the entire array (not element-by-element as you might expect). 
# Use the bitwise operators & and | instead.


# logical_and(x1, x2, /[, out, where, ...])
# Compute the truth value of x1 AND x2 element-wise.
print(np.logical_and(True, False))
# False
print(np.logical_and([True, False], [False, False]))
# [False False]
x = np.arange(5)
print(np.logical_and(x>1, x<4))
# [False False  True  True False]
# The & operator can be used as a shorthand for np.logical_and on boolean ndarrays.
a = np.array([True, False])
b = np.array([False, False])
print(a & b)
# [False False]


# logical_or(x1, x2, /[, out, where, casting, ...])
# Compute the truth value of x1 OR x2 element-wise.
print(np.logical_or(True, False))
# True
print(np.logical_or([True, False], [False, False]))
# [ True False]
x = np.arange(5)
print(np.logical_or(x < 1, x > 3))
# [ True False False False  True]
# The | operator can be used as a shorthand for np.logical_or on boolean ndarrays.
a = np.array([True, False])
b = np.array([False, False])
print(a | b)
# [ True False]


# logical_xor(x1, x2, /[, out, where, ...])
# Compute the truth value of x1 XOR x2, element-wise.
print(np.logical_xor(True, False))
# True
print(np.logical_xor([True, True, False, False], [True, False, True, False]))
# [False  True  True False]
x = np.arange(5)
print(np.logical_xor(x < 1, x > 3))
# [ True False False False  True]
# Simple example showing support of broadcasting
print(np.logical_xor(0, np.eye(2)))
# [[ True False]
#  [False  True]]


# logical_not(x, /[, out, where, casting, ...])
# Compute the truth value of NOT x element-wise.
print(np.logical_not(3))
# False
print(np.logical_not([True, False, 0, 1]))
# [False  True  True False]
x = np.arange(5)
print(np.logical_not(x<3))
# [False False False  True  True]


# Warning
# The bit-wise operators & and | are the proper way to perform element-by-element array comparisons. 
# Be sure you understand the operator precedence: 
# (a > 2) & (a < 5) is the proper syntax because a > 2 & a < 5 will result in an error due to the fact that 2 & a is evaluated first.


# maximum(x1, x2, /[, out, where, casting, ...])
# Element-wise maximum of array elements.
print(np.maximum([2, 3, 4], [1, 5, 2]))
# [2 5 4]
print(np.maximum(np.eye(2), [0.5, 2])) # broadcasting
# [[1.  2. ]
#  [0.5 2. ]]
print(np.maximum([np.nan, 0, np.nan], [0, np.nan, np.nan]))
# [nan nan nan]
print(np.maximum(np.Inf, 1))
# inf


# Tip
# The Python function max() will find the maximum over a one-dimensional array, but it will do so using a slower sequence interface. 
# The reduce method of the maximum ufunc is much faster. 
# Also, the max() method will not give answers you might expect for arrays with greater than one dimension. 
# The reduce method of minimum also allows you to compute a total minimum over an array.


# minimum(x1, x2, /[, out, where, casting, ...])
# Element-wise minimum of array elements.
print(np.minimum([2, 3, 4], [1, 5, 2]))
# [1 3 2]
print(np.minimum(np.eye(2), [0.5, 2])) # broadcasting
# [[0.5 0. ]
#  [0.  1. ]]
print(np.minimum([np.nan, 0, np.nan],[0, np.nan, np.nan]))
# [nan nan nan]
print(np.minimum(-np.Inf, 1))
# -inf


# Warning
# the behavior of maximum(a, b) is different than that of max(a, b). 
# As a ufunc, maximum(a, b) performs an element-by-element comparison of a and b and chooses each element of the result according to which element in the two arrays is larger. 
# In contrast, max(a, b) treats the objects a and b as a whole, looks at the (total) truth value of a > b and uses it to return either a or b (as a whole). 
# A similar difference exists between minimum(a, b) and min(a, b).


# fmax(x1, x2, /[, out, where, casting, ...])
# Element-wise maximum of array elements.
print(np.fmax([2, 3, 4], [1, 5, 2]))
# [2 5 4]
print(np.fmax(np.eye(2), [0.5, 2]))
# [[1.  2. ]
#  [0.5 2. ]]
print(np.fmax([np.nan, 0, np.nan],[0, np.nan, np.nan]))
# [ 0.  0. nan]


# fmin(x1, x2, /[, out, where, casting, ...])
# Element-wise minimum of array elements.
print(np.fmin([2, 3, 4], [1, 5, 2]))
# [1 3 2]
print(np.fmin(np.eye(2), [0.5, 2]))
# [[0.5 0. ]
#  [0.  1. ]]
print(np.fmin([np.nan, 0, np.nan],[0, np.nan, np.nan]))
# [ 0.  0. nan]