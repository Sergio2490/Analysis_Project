# 3) Диаграмма рассеивания

import matplotlib.pyplot as plt

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.title("Тестовая диаграмма рассеивания")

plt.show()
