#Дз2.
# Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
#
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)  # массив1 из 5 случайных чисел
y = np.random.rand(5) # массив2 из 5 случайных чисел
print(x, y)

plt.scatter(x, y)
plt.title('Диаграмма рассеяния 5-ти случайных чисел')
plt.xlabel('ось X')
plt.ylabel('Ось Y')
plt.show()

