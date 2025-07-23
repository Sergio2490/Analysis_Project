# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe())

#xau_usd.csv - данные о курсе золота к доллару с 01.01.2020 по 11.04.2024

import pandas as pd

df = pd.read_csv('xau_usd.csv', delimiter=';') #Загружаем набор данных из csv в датафрейм - переменную df

print(df.head())  #Выводим первые 5 строк

df.drop('Vol.', axis=1, inplace=True)  #Удаляем столбец "Vol.", так как в скачанном csv он все равно пустой
print(df)

print(df.info())  #Output a base data about dataframe

#Чтобы правильно выводились min, max, mean - уберем разделители тысяч ',' , проценты и пробелы и преобразуем строковые значения во float
# Список столбцов, которые нужно преобразовать
cols = ['Price', 'Open', 'High', 'Low', 'Change %']

for col in cols:
    # Удаляем запятые (тысячные), %, пробелы — и переводим в float
    df[col] = (
        df[col]
        .str.replace(',', '')         # убираем разделители тысяч
        .str.replace('%', '')         # убираем знак процента
        .str.strip()                  # убираем пробелы
        .astype(float)                # превращаем в float
    )

print(df.describe())  #Output a statistics about dataframe
