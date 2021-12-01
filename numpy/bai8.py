# Để bỏ qua các phần tử có giá trị nan trong mảng khi tính mean và median, numpy cung cấp cho ta 2 hàm sau:

import numpy as np

x = np.array([2, np.nan, 5, 9])
print("mean x = ", np.nanmean(x))
print("Median x = ", np.nanmedian(x))

# Nếu như sử dụng mean va median thông thường thì kết quả trả về sẽ là nan:
print("mean x = ", np.mean(x))
print("median x = ", np.median(x))