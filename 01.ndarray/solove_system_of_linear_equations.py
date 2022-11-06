# 線型方程式系とは、同時に成立する複数の線型方程式（一次方程式）の組のことである。
# 複数の方程式の組み合わせを方程式系あるいは連立方程式と呼ぶことから、
# 線型方程式系のことを一次方程式系、連立線型方程式、連立一次方程式等とも呼ぶこともある。

import numpy as np

# 次の連立方程式を解く
#  x +  y =  9
# 2x + 4y = 22

# 係数行列
matrix_a = np.array([[1, 1], [2, 4]])
print(matrix_a)
# [[1 2]
#  [3 4]]

# 定数行列
const_a = np.array( [9, 22])
print(const_a)
# [9 22]
 
# 連立方程式の解
var_a = np.linalg.solve(matrix_a, const_a)
print(var_a)
# [7. 2.]

# もとの方程式に代入して検算する
print(  var_a[0] +   var_a[1])
# 9.0
print(2*var_a[0] + 4*var_a[1])
# 22.0

#  x +  y − z =  6
#  x + 2y + z = 12
# 2x + 3y − z =  2

matrix_b = np.array([[1, 1, -1],[1, 2, 1],[2, 3, -1]])
print(matrix_b)
# [[ 1  1 -1]
#  [ 1  2  1]
#  [ 2  3 -1]]

const_b = np.array( [6,12,2])
print(const_b)
# [ 6 12  2]

# 連立方程式の解
var_b = np.linalg.solve(matrix_b, const_b)
print(var_b)
# [ 48. -26.  16.]

# もとの方程式に代入して検算する
print(  var_b[0] +   var_b[1] - var_b[2])
# 6.0
print(  var_b[0] + 2*var_b[1] + var_b[2])
# 12.0
print(2*var_b[0] + 3*var_b[1] - var_b[2])
# 2.0