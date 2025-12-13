tasks = [("Вивчити Python", False), ("Купити овочі", False)]

tasks[0] = (tasks[0][0], True)

for t in tasks:
    print(t[0], "Виконано" if t[1] else "Не виконано")
