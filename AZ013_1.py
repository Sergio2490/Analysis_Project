import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
#print(df.info())  #инфо
#print(df.describe())  № статистич данные - мин, макс, среднее
#print(df['Country name']) #выводим столбец
#print(df[['Country name', 'Regional indicator']])  #выводим несколько столбцов
#print(df.loc[56]) #выводим строчку по индексу
#print(df.loc[56, 'Healthy life expectancy'])
print(df[df['Healthy life expectancy'] > 0.7])

