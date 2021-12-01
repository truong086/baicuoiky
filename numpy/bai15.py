# np.random.binomial, hàm này thể hiện xác suất để x thành công trong n phép thử, với xác suất
# thành công p của mỗi phép thử

import numpy as np

coins = np.random.binomial(20, 0.5, 10) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print(coins)
print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())
