# Với nhiều hàm tính toán, ta có thể tính mane theo từng trục nếu là mảng nhiều chiều
import numpy as np

x = np.array([[1, 2], [3, 4]])
print("Mean x = ", np.mean(x))
print("median x axis = 0:", np.median(x, axis=0))
print("median x axis = 1:", np.median(x, axis=1))