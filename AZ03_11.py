import matplotlib.pyplot as plt

x = [2, 6, 8,14, 20]
y = [6, 4, 10, 12, 16]  # создали 2 списка

#теперь м создать график
plt.plot(x, y)
plt.title("Пример простого линейного графика")  #название графика
plt.xlabel("Ось Х")
plt.ylabel("Ось У")

plt.show()


