# Lưu ý là với định dạng single precision (float32) mean có thể không chính xác với các mảng lớn

import numpy as np

a = np.zeros((2, 512 * 512), dtype = np.float32)
a[0, :] = 1.0
a[1, :] = 0.1

print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))
print("mean a = ", np.mean(a, dtype=np.float64))
