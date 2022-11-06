

import numpy as np


matrix_a = np.array([[1, 2], [3, 4]])
print(matrix_a)
# [[1 2]
#  [3 4]]

inverse_a = np.linalg.inv(matrix_a)
print(inverse_a)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 検算１：二次正方行列の場合は逆行列の公式を使う
# A = ([a, b],[c, d])の場合
# A-1 = 1/(ad-bc)([d, -b],[-c, a])
inverse_a = 1/(matrix_a[0,0]*matrix_a[1,1] - matrix_a[0,1]*matrix_a[1,0])*np.array([[matrix_a[1,1],-1*matrix_a[0,1]],[-1*matrix_a[1,0],matrix_a[0,0]]])
print(inverse_a)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 検算２：元の行列と逆行列の積が単位行列であることを利用する
matrix_e = np.dot(matrix_a, inverse_a)
print(matrix_e)
# [[1.0000000e+00 0.0000000e+00]
#  [8.8817842e-16 1.0000000e+00]]
# 可読性のために丸める
print(np.round(matrix_e))
# [[1. 0.]
#  [0. 1.]]
# 単位行列になっていることが分かる。

