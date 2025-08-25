# Это AZ02 -выбросы
import pandas as pd
import matplotlib.pyplot as plt

# Создадим простой словарик, чт сделать из него датафрейм
data = {'value': [1,2,2,3,3,3,4,4,4,5,6,7,8,9,10,55]}

df = pd.DataFrame(data)  #Сделали из словаря датафрейм

# 1-й вариант - гистограмма
#df['value'].hist() #Рисуем гистограмму
#plt.show() #Показываем гистограмму

#2-й вариант
df.boxplot(column='value')
plt.show()
#print(df.describe())

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.76)
IQR = Q3 - Q1  #IQR - межквартильный размах

downside = Q1 - 1.5 * IQR  #нижняя граница
upside = Q3 + 1.5 * IQR  #верхняя граница

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]  #убираем выбросы, берем значения только из диапазона

df_new.boxplot(column='value')
plt.show()
