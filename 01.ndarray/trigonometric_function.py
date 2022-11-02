# NumPyの三角関数

# NumPyをインポートする
import numpy as np

# 円周率(π)
# np.piで表示できる。
print(np.pi)
# 3.141592653589793

# 度からラジアンへの変換
# np.radians()またはnp.deg2rad()を使う。
print(np.radians(90))
# 1.5707963267948966
print(np.deg2rad(90))
# 1.5707963267948966

# 配列を使うこともできる。
print(np.radians([0, 90, 180, 270]))
# [0.         1.57079633 3.14159265 4.71238898]
print(np.deg2rad([0, 90, 180, 270]))
# [0.         1.57079633 3.14159265 4.71238898]

# ラジアンから度への変換
# np.degrees()またはnp.rad2deg()を使う。
print(np.degrees(np.pi/2))
# 90.0
print(np.rad2deg(np.pi/2))
# 90.0

# 配列を使うこともできる。
print(np.degrees([0, np.pi/2, np.pi, np.pi*3/2]))
# [  0.  90. 180. 270.]
print(np.rad2deg([0, np.pi/2, np.pi, np.pi*3/2]))
# [  0.  90. 180. 270.]


# 正弦(sin)
# np.sin()を使う。ラジアンで指定する。
print(np.sin(1.57079633))
# 1.0
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.sin(np.radians(90)))
# 1.0
# 配列を使うこともできる。
print(np.sin(np.radians([0, 90, 180, 270])))
# [ 0.0000000e+00  1.0000000e+00  1.2246468e-16 -1.0000000e+00]
# ※結果に誤差が生じている。
# 　値を丸めたい場合はnp.round()を使う。
print(np.round(np.sin(np.radians([0, 90, 180, 270]))))
# [ 0.  1.  0. -1.]

# 余弦(cos) 
# np.cos()を使う。ラジアンで指定する。
print(np.cos(1.57079633))
# -3.205103454691839e-09
print(np.round(np.cos(1.57079633)))
# -0.0
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.cos(np.radians(90)))
# 6.123233995736766e-17
# 配列を使うこともできる。
print(np.cos(np.radians([0, 90, 180, 270])))
# [ 1.0000000e+00  6.1232340e-17 -1.0000000e+00 -1.8369702e-16]
# ※結果に誤差が生じている。
# 　値を丸めたい場合はnp.round()を使う。
print(np.round(np.cos(np.radians([0, 90, 180, 270]))))
# [ 1.  0. -1. -0.]


# 正接(tan)
# np.tan()を使う。ラジアンで指定する。
print(np.tan(3.141592653589793))
# -1.2246467991473532e-16
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.tan(np.radians(45)))
# 0.9999999999999999
# 配列を使うこともできる。
print(np.tan(np.radians([0, 30, 45, 90])))
# [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.63312394e+16]
# 値を丸めたい場合はnp.round()を使う。
print(np.round(np.tan(np.radians([0, 30, 45, 90]))))
# [0.00000000e+00 1.00000000e+00 1.00000000e+00 1.63312394e+16]

# 逆正弦
# np.arcsin()を使う。ラジアンで指定する。
print(np.arcsin(0))
# 0.0
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.arcsin(np.radians(0)))
# 0.0
# 配列を使うこともできる。
print(np.arcsin(np.radians([0, 15, 30, 45])))
# [0.         0.26488615 0.55106958 0.90333911]
# 配列を使うこともできる。
print(np.arcsin([0, (np.pi)/8, (np.pi)/6, (np.pi)/4]))
# [0.         0.26488615 0.55106958 0.90333911]

# 逆余弦
# np.arccos()を使う。ラジアンで指定する。
print(np.tan(3.141592653589793))
# -1.2246467991473532e-16
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.tan(np.radians(45)))
# 0.9999999999999999
# 配列を使うこともできる。
print(np.degrees(np.arccos([0, 0.5, 1])))
# 
# 配列を使うこともできる。
print(np.degrees([0, np.pi/2, np.pi, np.pi*3/2]))
# 

# 逆正接
# np.arctan()またはnp.arctan2()を使う。ラジアンで指定する。
print(np.tan(3.141592653589793))
# -1.2246467991473532e-16
# 角度で指定する場合はnp.radians()またはnp.deg2rad()で変換すると可読性が上がる。
print(np.tan(np.radians(45)))
# 0.9999999999999999
# 配列を使うこともできる。
print(np.degrees(np.arctan([0, 1, np.inf])))
# 
# 配列を使うこともできる。
print(np.degrees([0, np.pi/2, np.pi, np.pi*3/2]))
# 
