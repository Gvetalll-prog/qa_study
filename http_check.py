import requests
#Список адресов для игры со статусами

urls = [
"https://google.com",
"https://google.com/404",
"http://httpbin.org/status/200",
"http://httpbin.org/status/300",
"http://httpbin.org/status/400",
"http://httpbin.org/status/500"
]

print("--- ЗАПУСК HTTP СКАНЕРА ---")

for link in urls:
    try:
    # Делаем реальный запрос к сайту
        result = requests.get(link, timeout=5)
        # Печатаем код ответа (те самые 200, 404)
        print(f"Адрес: {link} | Код: {result.status_code}")
    
    except:
        print(f"Адрес: {link} | Ошибка: Сайт недоступен")
    
print("--- ПРОВЕРКА ЗАВЕРШЕНА ---")