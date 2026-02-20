import os
#Список реальных адресов

sites = ["google.com", "google.com/404", "github.com", "github.com/404", "facebook.com", "noname.invalid"]

def check_site(hostname):
    # Выполняем команду ping в системе Linux
    # -c 1 означает отправить только 1 пакет
    # > /dev/null 2>&1 заставляет линукс не мусорить в терминал лишним текстом
        response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")

        if response == 0:
            return f"Сайт [{hostname}] -> OK"
        else:
            return f"Сайт [{hostname}] -> ERROR"
    
print("--- ПРОВЕРКА РЕАЛЬНОГО СОЕДИНЕНИЯ ---")

for site in sites:
    print(check_site(site))
print("--- ПРОВЕРКА ЗАВЕРШЕНА ---")