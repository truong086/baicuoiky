import matplotlib.pyplot as plt
import numpy as np

phantichcorechip = ["core-i3","core-i5", "core-i7", "core-i9", "core-i9k"]
dungnhieu = [20, 25, 15, 10, 20]
Explode = [0,0.1,0,0,0]

plt.pie(dungnhieu,explode=Explode,labels=phantichcorechip,shadow=True, startangle=45)
plt.axis('equal')
plt.legend(title="Chú thích")

plt.show()