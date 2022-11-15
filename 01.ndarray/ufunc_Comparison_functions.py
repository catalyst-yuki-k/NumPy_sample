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

# less_equal(x1, x2, /[, out, where, casting, ...])
# Return the truth value of (x1 <= x2) element-wise.

# not_equal(x1, x2, /[, out, where, casting, ...])
# Return (x1 != x2) element-wise.

# equal(x1, x2, /[, out, where, casting, ...])
# Return (x1 == x2) element-wise.