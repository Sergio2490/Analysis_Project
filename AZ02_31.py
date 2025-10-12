#Категориальные данные

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engeneering', 'Marketing', 'Engeneering', 'HR']
}

#Сделаем из этого словаря датафрейм
df = pd.DataFrame(data)

#Создадим категории - по полу и по департаменту
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

#print(df['gender'].cat.categories)
#print(df['department'].cat.categories)
print(df['department'].cat.codes)

#Добавим новую категорию
df['department'] = df["department"].cat.add_categories("Finance")
print(df["department"].cat.categories)

#Удалим категорию
df['department'] = df["department"].cat.remove_categories("HR")
print(df["department"].cat.categories)

print(df)