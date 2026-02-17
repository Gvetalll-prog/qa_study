from datetime import datetime # Импортируем инструмент для работы со временем
# Создаем переменную-флаг, которая разрешает циклу работать
is_active = True

while is_active == True:
        print("\n" + "="*30)
        print("Проверка возраста (для выхода введи 0)")

        # Спрашиваем год
        user_input = input("Введи год твоего рождения:")
        birth_year = int(user_input)

        # Проверяем: если ввели 0, выключаем цикл
        if birth_year == 0:
                is_active = False
                print("Программа завершена. Удачи в обучении!")

        # Иначе выполняем твою стандартную логику
        else:
                current_year = datetime.now().year # Эта команда сама возьмет 2026 (или 2027 потом)

                if birth_year > current_year:
                        print("Error! Это год из будущего! 🚀")
                else:
                    # Сюда мы попадем ТОЛЬКО если год не из будущего
                    age = current_year - birth_year
                    print(f"Сейчас тебе {age} лет.")

                    if age >= 18:
                        print("Доступ к курсу QA Automation разрешен. ✅")
                    else:
                        print("Доступ запрещен. Ты слишком молод. ❌")