def divide(a, b):
    try:
        result = a / b
        print(f"Результат деления:{result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    finally:
        print("Выполнение блока finally")


divide(10, 2)
divide(5, 0)
