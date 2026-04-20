# Д.з.3 Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цен
# у диванов  и вывести ее, а также сделать гистограмму цен на диваны

import requests
import re
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/kirov/category/divany-i-kresla'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

# Ищем все span с data-testid="price" и забираем число. В коде html: <span data-testid="price">84 054 <span>
prices = re.findall(r'data-testid="price">(\d{1,3}(?: \d{3})*)', html)
prices = [int(p.replace(' ', '')) for p in prices]

print(f"Найдено диванов: {len(prices)}")
print(f"Цены: {prices}")

# Сохраняем в CSV
df = pd.DataFrame({'price': prices})
df.to_csv('divan_prices.csv', index=False)

# Средняя цена
avg = df['price'].mean()
print(f"\nСредняя цена: {avg:,.0f} ₽")

# Гистограмма
plt.hist(prices, bins=15, edgecolor='black')
plt.axvline(avg, color='red', linestyle='dashed')
plt.title('Цены на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество диванов')
plt.savefig('histogram.png')
plt.show()