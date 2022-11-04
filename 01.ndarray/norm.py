import numpy as np
 
# numpy.linalg.normでベクトルのノルムを求められる。
# サンプルとして、ピタゴラス数の小さい２数を使用した２次元ベクトルのノルムを求める。
x = np.array([3, 4])
print(np.linalg.norm(x))
# 5.0
# 斜辺の長さとなっている

y = np.array([5, 12])
print(np.linalg.norm(y))
# 13.0

# 斜辺の長さとなっている

# ３次元以上でも同様にノルムを求められる。
z = np.array([2, 4, 4])
print(np.linalg.norm(z))
# 6.0
# 直方体の対角線の長さとなっている