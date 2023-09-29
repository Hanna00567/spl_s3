toys = {
    'Мяч': ['красный', 100, 5],
    'Кукла': ['синяя', 200, 10],
    'Автомобиль': ['зеленый', 150, 3],
    'Конструктор': ['желтый', 300, 7],
    'Плюшевый мишка': ['коричневый', 250, 2],
    'Пазл': ['серый', 180, 4]
}


def show_description():
    print("--Описание игрушек--")
    for toy, description in toys.items():
        print(toy + " - " + description[0])


def show_price():
    print("--Цены на игрушки--")
    for toy, description in toys.items():
        print(toy + " - " + str(description[1]))


def show_quantity():
    print("--Количество игрушек--")
    for toy, description in toys.items():
        print(toy + " - " + str(description[2]))


def show_info():
    print("--Информация об игрушках--")
    for toy, description in toys.items():
        print("Название: " + toy)
        print("Описание: " + description[0])
        print("Цена: " + str(description[1]))
        print("Количество: " + str(description[2]))
        print("----------------")


def buy_toy():
    total_price = 0
    print("--Покупка игрушек--")
    while True:
        toy = input("Введите название игрушки (n - выход): ")
        if toy == 'n':
            break
        if toy not in toys:
            print("Такой игрушки нет в магазине.")
            continue
        quantity = input("Введите количество: ")
        if not quantity.isdigit():
            print("Некорректное количество.")
            continue
        quantity = int(quantity)
        if quantity > toys[toy][2]:
            print("Недостаточно товара в магазине.")
            continue
        toys[toy][2] -= quantity
        total_price += toys[toy][1] * quantity
        print("Товар успешно добавлен в корзину.")
    print("Итоговая цена: " + str(total_price))
    print("--Обновленное количество--")
    show_quantity()


def goodbye():
    print("До свидания!")


while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")
    if choice == '1':
        show_description()
    elif choice == '2':
        show_price()
    elif choice == '3':
        show_quantity()
    elif choice == '4':
        show_info()
    elif choice == '5':
        buy_toy()
    elif choice == '6':
        goodbye()
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
    print("----------------")
