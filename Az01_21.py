import pandas as pd
import numpy as np

dates = pd.date_range('2022-07-26', period=10, freq='D')  #создаем даты - начю дата, сколько, интервал - 1 день (D)

#Создадим список значений, используя numpy

values = np.random.rand(10)  #создаем 10 случайных значений. Ранее - создали 10 дат.

df = pd.DataFrame({'Date': dates, 'Value': values})  #создаем словарь, а на его основе - создаем датафрейм




