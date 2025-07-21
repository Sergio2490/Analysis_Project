import pandas as pd

df = pd.read_csv('hh.csv', delimiter = ';')  #Сначала читаем csv-файл

#df['Test'] = [new for new in range(50)]

#print(df)

#df.drop('Test', axis = 1, inplace = True)  #Удаляем столбец Test
df.drop(49, axis = 0, inplace = True)
print(df)