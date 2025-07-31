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