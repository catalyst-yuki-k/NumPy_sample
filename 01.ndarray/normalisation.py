import numpy as np

# numpy.linalg.normでベクトルのノルムを求められる。
# ３次元以上でノルムを求めた場合、直方体の対角線の長さとなる。
matrix_a = np.array([2, 4, 4])
norm_a = np.linalg.norm(matrix_a)
print(norm_a)
# 6.0
 
# 元の配列をノルムで割ることで正規化された配列が作れる
matrix_e = matrix_a / norm_a 
print(matrix_e)
#  [0.33333333 0.66666667 0.66666667]
 
# ノルムを求めると1.0になっており、正規化されていることが分かる
norm_e = np.linalg.norm(matrix_e)
print(norm_e)
# 1.0