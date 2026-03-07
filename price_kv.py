#читаем файл prices.csv и преобразуем тхт в числовые значения -> cleaned.csv
import csv
import re

# Читаем исходный файл и преобразуем цены
cleaned_prices = []

with open('prices.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Пропускаем заголовок

    for row in reader:
        if row:  # Проверяем, что строка не пустая
            price_text = row[0]
            # Удаляем пробелы и суффикс "₽/мес."
            price_clean = re.sub(r'\s*₽/мес\.*$', '', price_text)
            # Убираем пробелы и преобразуем в целое число
            price_number = int(price_clean.replace(' ', ''))
            cleaned_prices.append([price_number])

# Сохраняем числовые значения в новый файл
with open('cleaned.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Price'])
    writer.writerows(cleaned_prices)

print(f"Обработано цен: {len(cleaned_prices)}")
print("Числовые значения сохранены в cleaned.csv")

# Для проверки выведем статистику
if cleaned_prices:
    prices_list = [price[0] for price in cleaned_prices]
    print(f"\nСтатистика по ценам:")
    print(f"Минимальная: {min(prices_list)}")
    print(f"Максимальная: {max(prices_list)}")
    print(f"Средняя: {sum(prices_list) // len(prices_list)}")

    # Выведем первые 5 цен для проверки
    print(f"\nПервые 5 цен:")
    for i, price in enumerate(prices_list[:5]):
        print(f"{i + 1}. {price}")