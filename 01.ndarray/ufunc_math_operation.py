# NumPyのndarrayの全要素に対し、要素ごとに処理を行い、結果をndarrayで返す関数をユニバーサル関数(ufunc)と呼ぶ
# ヒント
# オプションの出力引数を使用すると、大規模な計算のためにメモリを節約できます。
# 配列が大きい場合、複雑な式は、一時的な計算スペースの作成と (後で) 破棄のために、必要以上に時間がかかることがあります。
# たとえば、
# G = A * B + C
# は
# T1 = A * B;
# G = T1 + C;
# del T1
# と同等です。
# G = A * B;
# G += C
# と同じである
# G = A * B;
# add(G, C, G)
# ほど速く実行されます。

import numpy as np

# 加算
# add(x1, x2, /[, out, where, casting, order, ...])
# 要素ごとに引数を加算します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.add(matrix_x, matrix_y)
print(matrix_z)
# [5 7 9]

# 減算
# 
# 要素ごとに引数を減算します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.subtract(matrix_x, matrix_y)
print(matrix_z)
# [3 3 3]

# 乗算
# 
# 要素ごとに引数を乗算します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.multiply(matrix_x, matrix_y)
print(matrix_z)
# [ 4 10 18]

# 行列積
# 
# 2 つの配列の行列積。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.matmul(matrix_x, matrix_y)
print(matrix_z)
# 32

# 除算（余りなし、true_divideと同じ）
# 
# 引数を要素ごとに分割します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.divide(matrix_x, matrix_y)
print(matrix_z)
# [4.  2.5 2. ]

# 累乗和の対数
# 
# 入力の累乗和の対数。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.logaddexp(matrix_x, matrix_y)
print(matrix_z)
# [4.04858735 5.04858735 6.04858735]

# 累乗和の対数
# 
# 基数が2の場合の入力の累乗和の対数。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.logaddexp2(matrix_x, matrix_y)
print(matrix_z)
# [4.169925 5.169925 6.169925]

# 除算（余りなし、divideと同じ）
# 
# 引数を要素ごとに分割します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.true_divide(matrix_x, matrix_y)
print(matrix_z)
# [4.  2.5 2. ]

# 商
# 
# 入力の除算以下の最大の整数を返します。

matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.floor_divide(matrix_x, matrix_y)
print(matrix_z)
# [4 2 2]

# 各要素に”-1”を掛ける

matrix_x = np.array([-1, 2, -3])
matrix_z = np.negative(matrix_x)
print(matrix_z)
# [ 1 -2  3]

# 各要素に”+1”を掛ける（意味あるのか？？？）

matrix_x = np.array([-1, 2, -3])
matrix_z = np.positive(matrix_x)
print(matrix_z)
# [-1  2 -3]

# 累乗（型を保持する累乗関数）
# １番目の引数を２番目の引数で累乗する
# 累乗は英語でpower
# ２番目の引数は定数とすることができる
matrix_x = np.array([4, 5, 6])
const_y = 3
matrix_z = np.power(matrix_x,const_y)
print(matrix_z)
# [ 64 125 216]
# ２番目の引数は配列とすることができる。
# この時、１番目の配列の各要素は、２番目の配列の対応する要素で累乗される。
matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.power(matrix_x,matrix_y)
print(matrix_z)
# [  4  25 216]

# 累乗（整数を float にキャストする累乗関数）
# 引数が整数であっても結果は小数で表示される。
# １番目の引数を２番目の引数で累乗する
# ２番目の引数は定数とすることができる
matrix_x = np.array([4, 5, 6])
const_y = 3
matrix_z = np.float_power(matrix_x,const_y)
print(matrix_z)
# [ 64. 125. 216.]
# ２番目の引数は配列とすることができる。
# この時、１番目の配列の各要素は、２番目の配列の対応する要素で累乗される。
matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.float_power(matrix_x,matrix_y)
print(matrix_z)
# [  4.  25. 216.]

# 余り
# １番目の引数を２番目の引数で割った余りが戻り値となる。
matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.remainder(matrix_x,matrix_y)
print(matrix_z)
# [0 1 0]

# 余り
# １番目の引数を２番目の引数で割った余りが戻り値となる。
matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.mod(matrix_x,matrix_y)
print(matrix_z)
# [0 1 0]

# 負の被除数と除数の剰余演算の結果は、規約に拘束されます。
# fmodの場合、結果の符号は被除数の符号ですが、remainderの結果の符号は除数の符号です。
# このfmod関数は、Matlabのrem関数と同等です。
# fmodは被除数(割られる数)の符号が結果の符号になる。
# 下記の例では割られる側である[-3, -2, -1, 1, 2, 3]の符号と結果[-1  0 -1  1  0  1]の符号が一致している。
print(np.fmod([-3, -2, -1, 1, 2, 3], 2))
# [-1  0 -1  1  0  1]
# remainderは除数(割る数)の符号が結果の符号になる。
# 下記の例では割る側である2の符号と結果[1 0 1 1 0 1]の符号が一致している。
print(np.remainder([-3, -2, -1, 1, 2, 3], 2))
# [1 0 1 1 0 1]