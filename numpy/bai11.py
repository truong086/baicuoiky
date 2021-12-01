# Thống kê thứ tự (Oder statistics)

# Giá trị lớn nhất và nhỏ nhất

import numpy as np

x = np.array([[11, 12], [13, 14], [10, 9], [22, 21], [99, 100]])
print("x = ", x)

print("Giá trị lớn nhất là: ", np.amax(x))
print("Giá trị nhỏ nhất là: ", np.amin(x))
print("Giá trị lớn nhất của axis = 0 là: ", np.amax(x, axis=0))
print("Giá trị lớn nhất của axis = 1 là: ", np.amax(x, axis=1))