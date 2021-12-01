import matplotlib.pyplot as plt
import numpy as np

bieudophantichdienthoai = ["Iphone", "Samsung", "Oppo", "LG", "Xaomi"]
nuanamdau = [95, 85, 80, 78, 82]
cuoinam = [100, 90, 82, 80, 86]

index = np.arange(5)
width = 0.30

plt.bar(index, nuanamdau, width, color='yellow', label="Nửa năm đầu")
plt.bar(index, cuoinam,width, color='red', label="Cuối năm", bottom=cuoinam)

plt.title("Biểu đồ phân tích người dùng điện thoại trong 1 năm qua")
plt.xlabel("Phân tích bên trái")
plt.ylabel("Phân tích bên phải")
plt.xticks(index, bieudophantichdienthoai)

plt.legend(loc='best')
plt.show()