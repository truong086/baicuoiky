# numpy.random.uniform, hàm này sẽ sinh ra một mảng có giá trị phân phối đều (uniform distribution) trong một khoảng
# nhất định cho trước, hàm có cú pháp như sau:

# Khai báo thư viện của hàm
#import numpy.random

# Cú pháp của hàm
#numpy.random.uniform(low=0.0, high=1.0, size=None)

import numpy as np

u = np.random.uniform(size=4)
print(u)

# Mục đích của hàm này là tạo lên một dãy hoán vị, cú pháp: numpy.random.permutation(x)
p = np.random.permutation(10)
print(p)