# Ta có thêm bias vào như sau

import numpy as np

n = 10 # Tung 10 đồng xu trong 1 lần
p = 0.2 # bias cho mặt ngửa (Xác xuất cho mặt ngửa là 0.2)
l = 1000 # Số lần lặp

b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())