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

# 商と余り
# １番目の引数を２番目の引数で割った余りが戻り値となる。
# 戻り値は商の配列と余りの配列である。
matrix_x = np.array([4, 5, 6])
matrix_y = np.array([1, 2, 3])
matrix_z = np.divmod(matrix_x,matrix_y)
print(matrix_z)
# (array([4, 2, 2]), array([0, 1, 0]))

# 絶対値
matrix_x = np.array([-1, 2, -3])
matrix_z = np.absolute(matrix_x)
print(matrix_z)
# [1 2 3]
# 複素数の場合、実部と虚部の二乗平均(斜辺の長さ)
print(np.absolute(3 + 4j))
# 5.0

# 絶対値(戻り値は必ず小数)
matrix_x = np.array([-1, 2, -3])
matrix_z = np.fabs(matrix_x)
print(matrix_z)
# [1. 2. 3.]

# 四捨五入後の整数(戻り値は必ず小数)
matrix_x = np.array([-1.2, 2.7, -3.5])
matrix_z = np.rint(matrix_x)
print(matrix_z)
# [-1.  3. -4.]

# 符号
# 正の数に対して1、負の数に対して-1を返す。
# ここで使用される定義は、x/√(x*x)で、これは一般的な代替手段であるx/|x|とは異なる。
matrix_x = np.array([-1.2, 2.7, -3.5])
matrix_z = np.sign(matrix_x)
print(matrix_z)
# [-1.  1. -1.]
# 0に対して0を返す。
print(np.sign(0))
# 0
# 虚部に対しては常に0jを返す
print(np.sign(3 + 4j))
# (1+0j)

# ヘヴィサイドの階段関数
# heaviside(x1, x2)において
# x1 < 0  のとき 0
# x1 == 0 のとき x2
# x1 > 0  のとき 1
matrix_x = np.array([-1.5, 0, 2.0])
const_y  = 0.5
matrix_z = np.heaviside(matrix_x,const_y)
print(matrix_z)
# [0.  0.5 1. ]
matrix_x = np.array([-1.5, 0, 2.0])
const_y  = 1
matrix_z = np.heaviside(matrix_x,const_y)
print(matrix_z)
# [0. 1. 1.]

# 複素共役
# 複素数の虚部を反数にした複素数をとる操作（写像）のこと
# conjはconjugateのエイリアスである
print(np.conjugate(1+2j))
# (1-2j)
print(np.conjugate(np.eye(2) + 1j * np.eye(2)))
# [[1.-1.j 0.-0.j]
#  [0.-0.j 1.-1.j]]

# 指数
# 入力配列のすべての要素の指数を計算します。
# exp(x) の大きさと位相を複素平面にプロットします。
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 100)
xx = x + 1j * x[:, np.newaxis]
out = np.exp(xx)

plt.subplot(121)
plt.imshow(np.abs(out),extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='gray')
plt.title('Magnitude of exp(x)')

plt.subplot(122)
plt.imshow(np.angle(out),extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv')
plt.title('Phase (angle) of exp(x)')
plt.show()

# 指数
# 入力配列のすべての p に対して 2**p を計算します。
print(np.exp2([2, 3]))
# [4. 8.]

# 対数
# 要素ごとの自然対数。
print(np.log([1, np.e, np.e**2, 0]))
# [  0.   1.   2. -inf]

# 対数
# x の 2 を底とする対数。
x = np.array([0, 1, 2, 2**4])
print(np.log2(x))
# [-inf   0.   1.   4.]
xi = np.array([0+1.j, 1, 2+0.j, 4.j])
print(np.log2(xi))
# [0.+2.26618007j 0.+0.j         1.+0.j         2.+2.26618007j]

# 自然対数
# 入力配列の 10 を底とする対数を要素ごとに返します。
print(np.log10([1e-15, -3.]))
# [-15.  nan]

# 指数関数exp(x)-1
# 配列内のすべての要素について exp(x) - 1 を計算します。
print(np.expm1(1e-10))
# 1.00000000005e-10

print(np.exp(1e-10) - 1)
# 1.000000082740371e-10

# 対数関数log(1 + x)
# 配列内のすべての要素について log(1 + x) を計算します。
print(np.log1p(1e-99))
# 

print(np.log(1 + 1e-99))
# 

# 平方根(非負)
# 配列内のすべての要素について非負の平方根を計算します。
print(np.sqrt([1,4,9]))
# [ 1.,  2.,  3.]
print(np.sqrt([4, -1, -3+4J]))
# [ 2.+0.j,  0.+1.j,  1.+2.j]
print(np.sqrt([4, -1, np.inf]))
# [ 2., nan, inf]

# 平方根
print(np.square([-1j, 1]))
# [-1.-0.j,  1.+0.j]

# 三乗根
print(np.cbrt([1,8,27]))
# [ 1.,  2.,  3.]

# 逆数
print(np.reciprocal(2.))
# 0.5
print(np.reciprocal([1, 2., 3.33]))
# [ 1.       ,  0.5      ,  0.3003003]

# 最大公約数
# |x1|と|x2|の最大公約数を返す
print(np.gcd(12, 20))
# 4
print(np.gcd.reduce([15, 25, 35]))
# 5
print(np.gcd(np.arange(6), 20))
# [20,  1,  2,  1,  4,  5]

# 最小公倍数
# |x1|と|x2|の最小公倍数を返す
print(np.lcm(12, 20))
# 60
print(np.lcm.reduce([3, 12, 20]))
# 60
print(np.lcm.reduce([40, 12, 20]))
# 120
print(np.lcm(np.arange(6), 20))
# array([ 0, 20, 20, 60, 20, 20])