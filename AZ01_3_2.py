import pandas as pd


#df = pd.read_csv('animal.csv')
#print(df)

#df.fillna(0, inplace=True)  #заполнили постые значения нулями 0.0
#df.dropna(inplace=True)  #а здесь - целиком удаляем строки с пустыми значениями
#group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()  #группирует по полю Пища и для этих 2-х групп вычисляем среднюю прод жизни животных
#print(group)

data = {
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
     'City': ['New York', 'Los Angeles', 'Chicago']
}  #создаем словарь

df = pd.DataFrame(data)  #создаем датафрейм

df.to_csv('output.csv', index = False)  #сохраняем датафрейм в csv

