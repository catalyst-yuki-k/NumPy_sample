import numpy as np
import matplotlib.pylab as plt
from math import pi

# sin(x, /[, out, where, casting, order, ...])
# Trigonometric sine, element-wise.
print(np.sin(np.pi/2.))
# 1.0
print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. ))
# [0.         0.5        0.70710678 0.8660254  1.        ]
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()


#cos(x, /[, out, where, casting, order, ...])
#Cosine element-wise.
print(np.cos(np.array([0, np.pi/2, np.pi])))
# [ 1.000000e+00  6.123234e-17 -1.000000e+00]
# Example of providing the optional output parameter
out1 = np.array([0], dtype='d')
out2 = np.cos([0.1], out1)
print(out2 is out1)
# True
# Example of ValueError due to provision of shape mis-matched `out`
#print(np.cos(np.zeros((3,3)),np.zeros((2,2))))
#Traceback (most recent call last):
#  File "c:\github\repository\NumPy_sample\01.ndarray\ufunc_Trigonometric_functions.py", line 27, in <module>
#    print(np.cos(np.zeros((3,3)),np.zeros((2,2))))
#ValueError: operands could not be broadcast together with shapes (3,3) 


# tan(x, /[, out, where, casting, order, ...])
#Compute tangent element-wise.
print(np.tan(np.array([-pi,pi/2,pi])))
# [ 1.22464680e-16  1.63312394e+16 -1.22464680e-16]
# Example of providing the optional output parameter illustrating
# that what is returned is a reference to said parameter
out1 = np.array([0], dtype='d')
out2 = np.cos([0.1], out1)
print(out2 is out1)
# True
# Example of ValueError due to provision of shape mis-matched `out`
#print(np.cos(np.zeros((3,3)),np.zeros((2,2))))
#Traceback (most recent call last):
#  File "c:\github\repository\NumPy_sample\01.ndarray\ufunc_Trigonometric_functions.py", line 44, in <module>
#    print(np.cos(np.zeros((3,3)),np.zeros((2,2))))
#ValueError: operands could not be broadcast together with shapes (3,3) (2,2)


# arcsin(x, /[, out, where, casting, order, ...])
#Inverse sine, element-wise.
print(np.arcsin(1))     # pi/2
# 1.5707963267948966
print(np.arcsin(-1))    # -pi/2
# -1.5707963267948966
print(np.arcsin(0))
# 0.0


# arccos(x, /[, out, where, casting, order, ...])
# Trigonometric inverse cosine, element-wise.
print(np.arccos([1, -1]))
# [ 0.        ,  3.14159265]
x = np.linspace(-1, 1, num=100)
plt.plot(x, np.arccos(x))
plt.axis('tight')
plt.show()


# arctan(x, /[, out, where, casting, order, ...])
# Trigonometric inverse tangent, element-wise.
print(np.arctan([0, 1]))
# [ 0.        ,  0.78539816]
print(np.pi/4)
# 0.7853981633974483
x = np.linspace(-10, 10)
plt.plot(x, np.arctan(x))
plt.axis('tight')
plt.show()


# arctan2(x1, x2, /[, out, where, casting, ...])
# Element-wise arc tangent of x1/x2 choosing the quadrant correctly.
x = np.array([-1, +1, +1, -1])
y = np.array([-1, -1, +1, +1])
print(np.arctan2(y, x) * 180 / np.pi)
# [-135.,  -45.,   45.,  135.]
print(np.arctan2([1., -1.], [0., 0.]))
# [ 1.57079633, -1.57079633]
print(np.arctan2([0., 0., np.inf], [+0., -0., np.inf]))
# [0.        , 3.14159265, 0.78539816]


# hypot(x1, x2, /[, out, where, casting, ...])
# Given the "legs" of a right triangle, return its hypotenuse.
print(np.hypot(3*np.ones((3, 3)), 4*np.ones((3, 3))))
# [[5. 5. 5.]
#  [5. 5. 5.]
#  [5. 5. 5.]]
print(np.hypot(3*np.ones((3, 3)), [4]))
# [[5. 5. 5.]
#  [5. 5. 5.]
#  [5. 5. 5.]]


# sinh(x, /[, out, where, casting, order, ...])
# Hyperbolic sine, element-wise.
print(np.sinh(0))
# 0.0
print(np.sinh(np.pi*1j/2))
# 1j
print(np.sinh(np.pi*1j)) # (exact value is 0)
# (-0+1.2246467991473532e-16j)
# Discrepancy due to vagaries of floating point arithmetic.
# Example of providing the optional output parameter
out1 = np.array([0], dtype='d')
out2 = np.sinh([0.1], out1)
print(out2 is out1)
# True
# Example of ValueError due to provision of shape mis-matched `out`
#print(np.sinh(np.zeros((3,3)),np.zeros((2,2))))
#Traceback (most recent call last):
#  File "c:\github\repository\NumPy_sample\01.ndarray\ufunc_Trigonometric_functions.py", line 124, in <module>
#    print(np.sinh(np.zeros((3,3)),np.zeros((2,2))))
#ValueError: operands could not be broadcast together with shapes (3,3) (2,2)


# cosh(x, /[, out, where, casting, order, ...])
# Hyperbolic cosine, element-wise.
print(np.cosh(0))
# 1.0
x = np.linspace(-4, 4, 1000)
plt.plot(x, np.cosh(x))
plt.show()


# tanh(x, /[, out, where, casting, order, ...])
# Compute hyperbolic tangent element-wise.
print(np.tanh((0, np.pi*1j, np.pi*1j/2)))
# [0.+0.00000000e+00j 0.-1.22464680e-16j 0.+1.63312394e+16j]
out1 = np.array([0], dtype='d')
out2 = np.tanh([0.1], out1)
print(out2 is out1)
# True
#print(np.tanh(np.zeros((3,3)),np.zeros((2,2))))
#Traceback (most recent call last):
#  File "c:\github\repository\NumPy_sample\01.ndarray\ufunc_Trigonometric_functions.py", line 149, in <module>
#    print(np.tanh(np.zeros((3,3)),np.zeros((2,2))))
#ValueError: operands could not be broadcast together with shapes (3,3) (2,2)


# arcsinh(x, /[, out, where, casting, order, ...])
# Inverse hyperbolic sine element-wise.
print(np.arcsinh(np.array([np.e, 10.0])))
# [1.72538256 2.99822295]

# arccosh(x, /[, out, where, casting, order, ...])
# Inverse hyperbolic cosine, element-wise.
print(np.arccosh([np.e, 10.0]))
# [1.65745445 2.99322285]
print(np.arccosh(1))
# 0.0


# arctanh(x, /[, out, where, casting, order, ...])
# Inverse hyperbolic tangent element-wise.
print(np.arctanh([0, -0.5]))
# [ 0.         -0.54930614]


# degrees(x, /[, out, where, casting, order, ...])
# Convert angles from radians to degrees.
rad = np.arange(12.)*np.pi/6
print(np.degrees(rad))
# [  0.  30.  60.  90. 120. 150. 180. 210. 240. 270. 300. 330.]
out = np.zeros((rad.shape))
r = np.degrees(rad, out)
print(np.all(r == out))
# True


# radians(x, /[, out, where, casting, order, ...])
# Convert angles from degrees to radians.
deg = np.arange(12.) * 30.
print(np.radians(deg))
# [0.         0.52359878 1.04719755 1.57079633 2.0943951  2.61799388  3.14159265 3.66519143 4.1887902  4.71238898 5.23598776 5.75958653] 
out = np.zeros((deg.shape))
ret = np.radians(deg, out)
print(ret is out)
# True


# deg2rad(x, /[, out, where, casting, order, ...])
# Convert angles from degrees to radians.
print(np.deg2rad(180))
# 3.141592653589793


# rad2deg(x, /[, out, where, casting, order, ...])
# Convert angles from radians to degrees.
print(np.rad2deg(np.pi/2))
# 90.0
