# NumPyをインポートする
import numpy as np

# ベクトルを作る
vector_x = np.array([1,2,3])

# ベクトルを表示する
print(vector_x)
# [1 2 3]

# 次元数を表示する
print(str(vector_x.ndim))
# 1

vector_x = np.array([1, 2, 3])
vector_y = np.array([4, 5, 6])
 
# ベクトルの和
vector_z = vector_x + vector_y
print(vector_z)
# [1 2 3]

# ベクトルの差
vector_z = vector_x - vector_y
print(vector_z)
# [-3 -3 -3]

# ベクトルの積(内積ではない)
vector_z = vector_x * vector_y
print(vector_z)
# [ 4 10 18]

# ベクトルの除
vector_z = vector_x / vector_y
print(vector_z)
# [0.25 0.4  0.5 ]

# ベクトルのスカラー倍
scalar_a = 100

vector_z = vector_x * scalar_a
print(vector_z)
# [100 200 300]

vector_z = scalar_a * vector_x
print(vector_z)
# [100 200 300]

# 内積
# np.dotで内積を計算することができます
 
vector_x = np.array([1, 2, 3])
vector_y = np.array([4, 5, 6])
 
vector_z = np.dot(vector_x, vector_y)
print(vector_z)
# 32

# 外積
# numpy.crossで求めることができます。

vector_x = np.array([1, 2, 3])
vector_y = np.array([4, 5, 6])
 
vector_z = np.cross(vector_x, vector_y)
print(vector_z)
# [-3  6 -3]
