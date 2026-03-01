#Сделаем график простой функции y = x^2

import numpy as np #чтобы создать массив
import matplotlib.pyplot as plt #чтобы построить график

x = np.linspace(-10, 10, 100) #равнораспределенный массив
y = x**2

plt.plot(x, y)
plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("График функции x**y")
plt.grid(True)
plt.show()
