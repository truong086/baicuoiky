# Median có thể tính theo các trục với mảng nhiều chiều:

import numpy as np

arr = np.array([[7, 4, 2], [3, 9, 5]])
print("Median arr (axis = 0)", np.median(arr, axis=0))
print("Median arr (axis = 1)", np.median(arr, axis=1))