from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import csv
import time

driver = webdriver.Firefox()

driver.get('https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')
time.sleep(5)  # Можно заменить на WebDriverWait для надежности


# Собираем все цены сразу
prices = driver.find_elements(By.XPATH, "//span[@data-mark = 'MainPrice']/span")

print(f"Найдено цен: {len(prices)}")  # Для отладки

# Сохраняем в CSV
with open('prices.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Price'])
    for price in prices:
        writer.writerow([price.text])

    print("Цены успешно сохранены в prices.csv")

    driver.quit()