from datetime import datetime

# ОПРЕДЕЛЯЕМ ФУНКЦИЮ (Logic for age check)
def check_access(year):
    current_year = datetime.now().year

    if year > current_year:
        return "ERROR: Future year"

    age = current_year - year

    # Vampires check (older than 100 years)
    if age > 100:
        return f"ERROR: Age is {age}. You are too old or a vampire!"
    
    if age >= 18:
        return f"SUCCESS: Age is {age}. Access granted."
    else:
        return f"DENIED: Age is {age}. Too young."

# ИСПОЛЬЗУЕМ ФУНКЦИЮ (Mein Loop)
active = True
print("---QA Age Checker System---")

while active:
    user_input = input("Enter birth year (or 'exit'): ")

    if user_input.lower() == 'exit':
        active = False
        print("system closed.")
    else:
        # Превращаем текст в число
        year_to_check = int(user_input)
        # Вызываем нашу функцию и получаем результат (result)
        result = check_access(year_to_check)
        print(result)