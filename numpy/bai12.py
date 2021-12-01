# Để bỏ qua các phần tử nan:

import numpy as np

x = np.array([[1, 2], [np.nan, 5], [10, 100], [80, np.nan], [60, 101]])

print("X = ", x)
print("Giá trị lớn nhất là: ", np.nanmax(x))
print("Giá trị nhỏ nhất là: ", np.nanmin(x))

# Phạm vi giá trị (Range)

# Phạm vi giá trị chính là max - min trong một dãy số
print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))