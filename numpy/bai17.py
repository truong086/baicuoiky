# Hàm numpy.random.rand trả về một mảng các số ngẫu nhiên mà mỗi phần tử là một số ngẫu nhiên có phân bố đều
# (uniform distribution) trong khoảng [0, 1):

import numpy as np

a = np.random.rand()
b = np.random.rand(4) # Mảng có 1x8 phần tử
c = np.random.rand(2, 3) # Mảng có 2x3 phần tử

print("a = ", a)
print("b = ", b)
print("c = ", c)