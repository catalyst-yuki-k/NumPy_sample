# https://numpy.org/doc/stable/reference/generated/numpy.dot.html

# NumPyをインポートする
import numpy as np

# ベクトルとベクトルの内積

vector_x = np.array([1, 2, 3])
vector_y = np.array([4, 5, 6])
 
# ベクトルとベクトルの内積は計算できる
# この例の場合、1*4 + 2*5 + 3*6
dot_xy = np.dot(vector_x,vector_y)
print(dot_xy)
# 32

# 次元数を表示する
print(str(dot_xy.ndim))
# 0

# 2次元ベクトルと2次元ベクトルの内積

vector_x = np.array([[1, 2, 3]])
vector_y = np.array([[4, 5, 6]])

# このままでは内積は計算できない
# dot_xy = np.dot(vector_x,vector_y)
# Traceback (most recent call last):
#   File "~~~~~~/dot_product.py", line ~~, in <module>
#     dot_xy = np.dot(vector_x,vector_y)
#   File "<__array_function__ internals>", line 5, in dot
# ValueError: shapes (1,3) and (1,3) not aligned: 3 (dim 1) != 1 (dim 0)

# vector_yを転置して列ベクトルに変換する
vector_yT = vector_y.T
print(vector_yT)
# [[4]
#  [5]
#  [6]]

# 行ベクトル×列ベクトルの内積を計算する
dot_xyT = np.dot(vector_x,vector_yT)
print(dot_xyT)
# [[32]]
# 結果が2次元であることに注意する

# 列ベクトル×行ベクトルの内積も可能
dot_yTx = np.dot(vector_yT,vector_x)
print(dot_yTx)
# [[ 4  8 12]
#  [ 5 10 15]
#  [ 6 12 18]]

# ベクトルと2次元ベクトルの内積

# ベクトルと行ベクトルの内積

vector_x = np.array([1, 2, 3])
vector_y = np.array([[4, 5, 6]])

# ベクトル×行ベクトルの内積は計算できない
# dot_xy = np.dot(vector_x,vector_y)
# Traceback (most recent call last):
#   File "~~~~~~/dot_product.py", line ~~, in <module>
#     dot_xy = np.dot(vector_x,vector_y)
#   File "<__array_function__ internals>", line 5, in dot
# ValueError: shapes (1,3) and (1,3) not aligned: 3 (dim 1) != 1 (dim 0)

# 行ベクトルを転置して列ベクトルにすることで計算できる
vector_yT = vector_y.T
dot_xyT = np.dot(vector_x,vector_yT)
print(dot_xyT)
# [32]

# 次元数を表示する
print(str(dot_xyT.ndim))
# 1
# 結果が1次元であることに注意する

# 行ベクトル×ベクトルの内積は計算できる
# この例の場合、4*1 + 5*2 + 6*3
dot_yx = np.dot(vector_y,vector_x)
print(dot_yx)
# [32]

# 次元数を表示する
print(str(dot_yx.ndim))
# 1
# 結果が1次元であることに注意する


# ベクトルと列ベクトルの内積

vector_x = np.array([1, 2, 3])
vector_y = np.array([[4],[5],[6]])

# ベクトル×列ベクトルの内積は計算できる
# この例の場合、1*4 + 2*5 + 3*6
dot_xy = np.dot(vector_x,vector_y)
print(dot_xy)
# [32]

# 次元数を表示する
print(str(dot_xy.ndim))
# 1
# 結果が1次元であることに注意する

# 列ベクトル×ベクトルの内積は計算できない
# dot_yx = np.dot(vector_y,vector_x)
# Traceback (most recent call last):
#   File "c:\github\repository\NumPy_sample\01.ndarray\dot_product.py", line 112, in <module>
#     dot_yx = np.dot(vector_y,vector_x)
#   File "<__array_function__ internals>", line 5, in dot
# ValueError: shapes (3,1) and (3,) not aligned: 1 (dim 1) != 3 (dim 0)

# 列ベクトルを転置して行ベクトルにすることで計算できる
# この例の場合、4*1 + 5*2 + 6*3
vector_yT = vector_y.T
dot_yTx = np.dot(vector_yT,vector_x)
print(dot_yTx)
# [32]

# 次元数を表示する
print(str(dot_yTx.ndim))
# 1
# 結果が1次元であることに注意する