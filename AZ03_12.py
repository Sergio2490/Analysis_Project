import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]

plt.hist(data, bins = 6)
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.title("Тестовая гистограмма")
plt.show()
