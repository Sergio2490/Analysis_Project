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

