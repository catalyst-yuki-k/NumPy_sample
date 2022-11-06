# 数学の線型代数学において、正方行列の跡あるいは対角和とは、主対角成分の総和である。

import numpy as np
 
matrix_a = np.array([[1, 2], [3, 4]])
print(matrix_a)
# [[1 2]
#  [3 4]]
 
trace_a = matrix_a.trace()
print(trace_a)
# 5

# 正方行列以外に対しても計算してしまうので注意

matrix_b = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix_b)
# [[1 2]
#  [3 4]
#  [5 6]]
 
trace_b = matrix_b.trace()
print(trace_b)
# 5
# ※1と4が足された

matrix_c = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_c)
# [[1 2 3]
#  [4 5 6]]
 
trace_c = matrix_c.trace()
print(trace_c)
# 6
# ※1と5が足された