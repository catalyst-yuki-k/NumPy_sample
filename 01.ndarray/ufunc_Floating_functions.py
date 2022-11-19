import numpy as np

# Recall that all of these functions work element-by-element over an array, returning an array output. 
# The description details only a single operation.

# isfinite(x, /[, out, where, casting, order, ...])
# Test element-wise for finiteness (not infinity and not Not a Number).
print(np.isfinite(1))
# True
print(np.isfinite(0))
# True
print(np.isfinite(np.nan))
# False
print(np.isfinite(np.inf))
# False
print(np.isfinite(np.NINF))
# False
print(np.isfinite(np.log(-1.)))
# RuntimeWarning: invalid value encountered in log
# False
print(np.isfinite(np.log(0)))
# RuntimeWarning: divide by zero encountered in log
# False
print(np.isfinite([np.log(-1.),1.,np.log(0)]))
# RuntimeWarning: invalid value encountered in log
# RuntimeWarning: divide by zero encountered in log
# [False  True False]
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isfinite(x, y))
# [0 1 0]
print(y)
# [0 1 0]


# isinf(x, /[, out, where, casting, order, ...])
# Test element-wise for positive or negative infinity.
print(np.isinf(np.inf))
# True
print(np.isinf(np.nan))
# False
print(np.isinf(np.NINF))
# True
print(np.isinf([np.inf, -np.inf, 1.0, np.nan]))
# [ True  True False False]
x = np.array([-np.inf, 0., np.inf])
y = np.array([2, 2, 2])
print(np.isinf(x, y))
# [1 0 1]
print(y)
# [1 0 1]


# isnan(x, /[, out, where, casting, order, ...])
# Test element-wise for NaN and return result as a boolean array.
print(np.isnan(np.nan))
# True
print(np.isnan(np.inf))
# False
print(np.isnan([np.log(-1.),1.,np.log(0)]))
# [ True False False]


# isnat(x, /[, out, where, casting, order, ...])
# Test element-wise for NaT (not a time) and return result as a boolean array.
print(np.isnat(np.datetime64("NaT")))
# True
print(np.isnat(np.datetime64("2016-01-01")))
# False
print(np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]")))
# [ True False]


# fabs(x, /[, out, where, casting, order, ...])
# Compute the absolute values element-wise.
print(np.fabs(-1))
# 1.0
print(np.fabs([-1.2, 1.2]))
# [ 1.2  1.2]


# signbit(x, /[, out, where, casting, order, ...])
# Returns element-wise True where signbit is set (less than zero).
print(np.signbit(-1.2))
# True
print(np.signbit(np.array([1, -2.3, 2.1])))
# [False  True False]


# copysign(x1, x2, /[, out, where, casting, ...])
# Change the sign of x1 to that of x2, element-wise.
print(np.copysign(1.3, -1))
# -1.3
print(1/np.copysign(0, 1))
# RuntimeWarning: divide by zero encountered in double_scalars
# inf
print(1/np.copysign(0, -1))
# RuntimeWarning: divide by zero encountered in double_scalars
# -inf
print(np.copysign([-1, 0, 1], -1.1))
# [-1. -0. -1.]
print(np.copysign([-1, 0, 1], np.arange(3)-1))
# [-1.  0.  1.]


# nextafter(x1, x2, /[, out, where, casting, ...])
# Return the next floating-point value after x1 towards x2, element-wise.

# spacing(x, /[, out, where, casting, order, ...])
# Return the distance between x and the nearest adjacent number.

# modf(x[, out1, out2], / [[, out, where, ...])
# Return the fractional and integral parts of an array, element-wise.

# ldexp(x1, x2, /[, out, where, casting, ...])
# Returns x1 * 2**x2, element-wise.

# frexp(x[, out1, out2], / [[, out, where, ...])
# Decompose the elements of x into mantissa and twos exponent.

# fmod(x1, x2, /[, out, where, casting, ...])
# Returns the element-wise remainder of division.

# floor(x, /[, out, where, casting, order, ...])
# Return the floor of the input, element-wise.

# ceil(x, /[, out, where, casting, order, ...])
# Return the ceiling of the input, element-wise.

# trunc(x, /[, out, where, casting, order, ...])
# Return the truncated value of the input, element-wise.

