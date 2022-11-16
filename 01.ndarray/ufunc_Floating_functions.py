import numpy as np

# Recall that all of these functions work element-by-element over an array, returning an array output. 
# The description details only a single operation.
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


# isfinite(x, /[, out, where, casting, order, ...])
# Test element-wise for finiteness (not infinity and not Not a Number).

# isinf(x, /[, out, where, casting, order, ...])
# Test element-wise for positive or negative infinity.

# isnan(x, /[, out, where, casting, order, ...])
# Test element-wise for NaN and return result as a boolean array.

# isnat(x, /[, out, where, casting, order, ...])
# Test element-wise for NaT (not a time) and return result as a boolean array.

# fabs(x, /[, out, where, casting, order, ...])
# Compute the absolute values element-wise.

# signbit(x, /[, out, where, casting, order, ...])
# Returns element-wise True where signbit is set (less than zero).

# copysign(x1, x2, /[, out, where, casting, ...])
# Change the sign of x1 to that of x2, element-wise.

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

