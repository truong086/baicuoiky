import matplotlib.pyplot as plt
import numpy as np

bieudodinhcao = ["HTML/CSS/JAVASCRIPT", "Java", "Python", "Ruby", "PHP"]
dohot = [80, 60, 70, 30, 50]
variance = [5,8,7,6,4]

plt.barh(bieudodinhcao,dohot,xerr=variance, color='yellow')
plt.title("Phân tích các ngôn ngữ đang hot hiện nay")
plt.xlabel("Biểu đồ đỉnh cao của phân tích bên trái")
plt.ylabel("Biểu đồ đỉnh cao của phân tích bên dưới")

plt.show()