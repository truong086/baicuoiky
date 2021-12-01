import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
divisions_average_marks = [70, 82, 73, 65, 68]

plt.bar(divisions,divisions_average_marks, color='red')
plt.title("Biểu đồ đỉnh cao siêu cấp víp pro")
plt.xlabel("Biểu đồ đỉnh cao siêu cấp víp pro bên trái")
plt.ylabel("Biểu đồ đỉnh cao siêu cấp víp pro ở dưới")
plt.show()