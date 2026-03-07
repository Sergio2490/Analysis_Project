#Построим график цен на квартиры
import csv
import matplotlib.pyplot as plt
import numpy as np

# Читаем цены из файла
prices = []

with open('cleaned.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Пропускаем заголовок

    for row in reader:
        if row:
            prices.append(int(row[0]))

# Создаем гистограмму
plt.figure(figsize=(12, 6))

# Основная гистограмма
n, bins, patches = plt.hist(prices, bins=15, edgecolor='black', alpha=0.7, color='skyblue')

# Добавляем подписи
plt.title('Распределение цен на аренду квартир', fontsize=16, fontweight='bold')
plt.xlabel('Цена (руб/мес)', fontsize=12)
plt.ylabel('Количество предложений', fontsize=12)

# Добавляем сетку для лучшей читаемости
plt.grid(True, alpha=0.3, linestyle='--')

# Добавляем подписи значений на столбцах
for i in range(len(n)):
    if n[i] > 0:
        plt.text(bins[i] + (bins[i + 1] - bins[i]) / 2, n[i], int(n[i]),
                 ha='center', va='bottom', fontsize=9)

# Добавляем статистическую информацию
plt.figtext(0.15, 0.85, f"Всего предложений: {len(prices)}", fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.figtext(0.15, 0.81, f"Средняя цена: {sum(prices) // len(prices):,} руб", fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.figtext(0.15, 0.77, f"Медианная цена: {sorted(prices)[len(prices) // 2]:,} руб", fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.figtext(0.15, 0.73, f"Мин цена: {min(prices):,} руб", fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.figtext(0.15, 0.69, f"Макс цена: {max(prices):,} руб", fontsize=10,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

# Настраиваем формат цен на оси X
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))

plt.tight_layout()
plt.show()