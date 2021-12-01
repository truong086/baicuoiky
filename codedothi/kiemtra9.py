import matplotlib.pyplot as plt
import numpy as np

phantichcachanglaptop = ["DELL", "ASUS", "ACER", "MSI", "Microsoft"]
sosanhnam2020 = [90, 98, 70, 95, 85]
sosanhnam2021 = [92, 100, 85, 98, 90]

index = np.arange(5)
width = 0.30

plt.bar(index,sosanhnam2020,width, color='blue', label='Năm 2020')
plt.bar(index+width, sosanhnam2021, width, color='grey', label='Năm 2021')
plt.title("Biểu đồ phân tích các hãng máy tính")

plt.xlabel("Phân tích bên trái")
plt.ylabel("Phân tích bên dưới")
plt.xticks(index+width/2, phantichcachanglaptop)

plt.legend(loc='best')
plt.show()