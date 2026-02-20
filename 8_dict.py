# Создаем словарь (Dictionary)
ticket = {
    "id": "QA-101",
    "title": "Login button not working",
    "priority": "High",
    "is_fixed": False
}

# 1. Выводим весь словарь, чтобы увидеть структуру
print("Full Ticket Data:", ticket)

# 2. Достаем конкретное значение по КЛЮЧУ
print(f"Checking Ticked: {ticket['id']}")
print(f"Issue Title: {ticket['title']}")

# 3. QA Логика: проверяем статус
if ticket["is_fixed"] ==False:
    print("STATUS: Verification failed. The bug is still there!")
else:
    print("STATUS: Verification passed. Close the ticket.")