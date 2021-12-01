import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)

plt.title("Biểu đồ bậc thang")
plt.xlabel("Bậc thang bên trái")
plt.ylabel("Bậc thang bên dưới")
plt.hist(x,10)

plt.show()