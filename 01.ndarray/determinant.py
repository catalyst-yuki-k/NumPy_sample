import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
print(matrix_a)
# [[1 2]
#  [3 4]]
 
determinant_a = np.linalg.det(matrix_a)
print(determinant_a)
# -2.0000000000000004
# 可読性のために丸める
print(np.round(determinant_a))
# -2.0