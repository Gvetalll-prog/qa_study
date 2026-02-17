from datetime import datetime

is_active = True
# Вместо списка [] создаем словарь {}
test_results = {}

while is_active == True:
    print("\n" + "="*25)
    user_input = input("Введи год (0 для выхода): ")
    birth_year = int(user_input)

    if birth_year == 0:
        is_active = False
    else:
        current_year = datetime.now().year

        if birth_year > current_year:
            status = "Ошибка! Год из будущего 🚀"
            print(status)
        else:
            age = current_year - birth_year
            if age>= 18:
                status = "Доступ разрешен ✅"
            else:
                status ="Слишком молод ❌"

            print(f"Возраст: {age}. {status}")

        # СОХРАНЯЕМ В СЛОВАРЬ: [Ключ] = Значение
        test_results[birth_year] = status

# ФИНАЛЬНЫЙ ОТЧЕТ
print("\n" + "### ИТОГОВЫЙ ОТЧЕТ ТЕСТИРОВАНИЯ ###")
for year, result in test_results.items():
    print(f"Год {year}: {result}")