# Tuy nhiên, nếu như phân khối bị lệch thì mean lúc này không còn nhiều ý nghĩa nữa, lúc đó ta sẽ dùng median, chẳng hạn:

import numpy as np

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 50293, 30432]) # 2 giá trị cuối lệch xa so với các giá trị trong dãy

print("Mean x = ", np.mean(freetuts_visitors))
print("Median x = ", np.median(freetuts_visitors))