# Trong numpy thì tìm bách phân vị được tính bởi hàm np.percentile(a, q, axis=None, iterpolation="linear"):

import numpy as np

scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])

print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='lower'))
print("Bách phân vị thứ 70: ", np.percentile(scores, 70, interpolation='higher'))
print("Bách vị phân thứ 70: ", np.percentile(scores, 70, interpolation='linear'))
print("Bách vị phân thứ 70: ", np.percentile(scores, 70, interpolation='nearest'))
print("Bách vị phân thứ 70: ", np.percentile(scores, 70, interpolation='midpoint'))

# Trung vị là giá trị giữa của dãy số được sắp xếp từ bé đến lớn, vì vậy bách phân vị thứ 50 chính là median của dãy số đó
print("Bách phân vị thứ 50: ", np.percentile(scores, 50))
print("Median = ", np.median(scores))

# Trong numpy thì tìm tứ phân vị được tính bởi hàm np.quantile(a, q, axis=None, iterpolation='linear'):
print("Q1 = ", np.quantile(scores, 0.25))
print("Q2 = ", np.quantile(scores, 0.5))
print("Q3 = ", np.quantile(scores, 0.75))