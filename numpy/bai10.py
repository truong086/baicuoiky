# Tương tự như mean và median, Numpy cũng cho chúng ta các hàm để bỏ qua các phần tử nan như sau:

import numpy as np

a = np.array([1, np.nan, 3, 4])
print("var = ", np.var(a))
print("std = ", np.std(a))
print("nanvar = ", np.nanvar(a))
print("nanstd = ", np.nanstd(a))