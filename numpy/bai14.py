import numpy as np

coins = np.random.randint(0, 2) # In ra số ngẫu nhiên trong khoảng 0 -> 2
print(coins)

nakr = np.random.randint(2, size=1000)
print(nakr.shape)
print("% số lần tung được mặt ngửa: ", (nakr == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (nakr == 1).mean() * 100)

