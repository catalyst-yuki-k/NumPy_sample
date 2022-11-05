# QR分解（QR decomposition）
# 行列AをA=QRが成り立つような直交行列Qと上三角行列Rに分解すること
# 行列Aを構成する列ベクトルa1,a2,…,anがすべて線形独立ならば
# シュミットの直交化法によって必ずQR分解をすることができる
# 最小二乗法では非正方行列Aにより定まる正規方程式A⊤Ax=A⊤cを解くことが必要だが、
# A=QRと分解するとRx=Q⊤cとなり、Rは上三角行列なので後退代入で簡単に解けるようになる

import numpy as np

matrix_a = np.array([[0, 1],[1, 1]])
print(matrix_a)
# [[0 1]
#  [1 1]]

# QR分解
matrix_q, matrix_r = np.linalg.qr(matrix_a)

print(matrix_q)
# [[ 0. -1.]
#  [-1.  0.]]

print(matrix_r)
# [[-1. -1.]
#  [ 0. -1.]]
