# NumPyの回転行列
# https://ja.wikipedia.org/wiki/%E5%9B%9E%E8%BB%A2%E8%A1%8C%E5%88%97

# NumPyをインポートする
import numpy as np

# 回転前の座標を決める
matrix_a = np.array([1, 0])

# 回転角を決める
rad = np.radians(45)

# １次変換の配列を決める
rot = np.array([[np.cos(rad), -np.sin(rad)],
                [np.sin(rad), np.cos(rad)]])

# 回転前の座標を表示する
print(matrix_a)
# [1 0]

# 回転前の座標に１次変換の配列をかける
matrix_b = np.dot(rot, matrix_a)

# 回転後の座標を表示する
print(matrix_b)
# [0.70710678 0.70710678]