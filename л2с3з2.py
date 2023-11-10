def proccess_input(data):
    if isinstance(data, list):
        negatives = 0
        neg_sum = 0
        for num in data:
            if num < 0:
                negatives += 1
                if negatives > 2:
                    neg_sum += num
        even_numbers = [num for num in data if num % 2 == 0]
        print("Сумма после второго элемента, меньше 0:", neg_sum)
        print("Чётные числа:", even_numbers)
    elif isinstance(data, set):
        if data:
            max_num = max(data)
            min_num = min(data)
            print("Максимальный элемент:", max_num)
            print("Минимальный элемент:", min_num)
    elif isinstance(data, int):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
                return True

        primes = [num for num in range(2, data) if is_prime(num)]
        print("Простые числа до", data, ":", primes)
    elif isinstance(data, str):
        digits = [char for char in data if char.isdigit()]
        print("Цифры в строке", digits)
    else:
        print("Недопустимый тип ввода")


def user_input():
    user_data = input("Введите данные(список, множество, число или строку):")

    if '[' in user_data:
        processed_data = eval(user_data)
        proccess_input(processed_data)
    elif '{' in user_data:
        processed_data = int(user_data)
        proccess_input(processed_data)
    else:
        processed_data = user_data
        proccess_input(processed_data)


user_input()
