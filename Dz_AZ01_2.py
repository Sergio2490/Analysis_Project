# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

# Удалим строки с пустыми значениями городов и зарплат - они нам только помешают в анализе
df.dropna(inplace=True)
print('\n---------\n', df)

# Сгруппируем по городам и посчитаем среднюю зарплату
group = df.groupby('City')['Salary'].mean()
print('\n---------\n',group)


