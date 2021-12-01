# Mean được sử dụng chủ yếu khi tập dữ liệu phân bố khá đồng đều với nhau, chẳng từ tập dữ liệu số người dùng truy cập
# Freetuts trong vòng 1 tuần qua như sau, ta có tính được trung bình mỗi ngày có bao nhiều người truy cập Freetuts

import numpy as np

freetuts_visitors = np.array([3776, 3112, 3476, 3319, 3559, 2121, 3462])
print("Số người truy cập trung bình mỗi ngày vào Freetuts là: ", np.median(freetuts_visitors))