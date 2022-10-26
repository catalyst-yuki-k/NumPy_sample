# NumPyをインポートする
import numpy as np

# 行ベクトルを作る
# 行ベクトルは2次元配列のため括弧は二重にする
# (内側の括弧は行を表す)
vector_row = np.array([[1,2,3]])

# ベクトルを表示する
print(vector_row)
# [[1 2 3]]

# 次元数を表示する
print(str(vector_row.ndim))
# 2

# 列ベクトルを作る
# 列ベクトルは2次元配列のため括弧は二重にし、行毎に括弧で区切る
vector_column = np.array([[1],[2],[3]])

# ベクトルを表示する
print(vector_column)
# [[1]
#  [2]
#  [3]]

# 次元数を表示する
print(str(vector_column.ndim))
# 2


# ベクトルから行ベクトルを作る
vector_x = np.array([1,2,3])
vector_row = vector_x.reshape(1,-1)

# ベクトルを表示する
print(vector_row)
# [[1 2 3]]

# 次元数を表示する
print(str(vector_row.ndim))
# 2

# ベクトルから列ベクトルを作る
vector_x = np.array([1,2,3])
vector_column = vector_x.reshape(-1,1)

# ベクトルを表示する
print(vector_column)
# [[1]
#  [2]
#  [3]]

# 次元数を表示する
print(str(vector_column.ndim))
# 2

# ベクトルを転置する
# べクトルは1次元配列なので、転置しても元のまま
vector_x.T

# ベクトルを表示する
print(vector_x)
# [1 2 3]

# 次元数を表示する
print(str(vector_x.ndim))
# 1

# 行ベクトルを転置する
vector_row.T

# ベクトルを表示する
print(vector_row)
# [1 2 3]

# 次元数を表示する
print(str(vector_row.ndim))
# 1

# 列ベクトルを転置する
vector_column.T

# ベクトルを表示する
print(vector_column)
# [[1]
#  [2]
#  [3]]

# 次元数を表示する
print(str(vector_column.ndim))
# 2

# 行ベクトルをベクトルにする
vector_row = np.array([[1,2,3]])
vector = vector_row.flatten()

# ベクトルを表示する
print(vector)
# [1 2 3]

# 次元数を表示する
print(str(vector.ndim))
# 1

# 列ベクトルをベクトルにする
vector_column = np.array([[1],[2],[3]])
vector = vector_column.flatten()

# ベクトルを表示する
print(vector)
# [1 2 3]

# 次元数を表示する
print(str(vector.ndim))
# 1