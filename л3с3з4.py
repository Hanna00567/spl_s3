import json

file_path = "firms_data.txt"
firms_data = []
average_profit = 0
firms_profit_dict = {}

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 4:
                firm_name, ownership_form, revenue, expenses = parts
                profit = int(revenue) - int(expenses)

                firms_data.append({
                    "name": firm_name,
                    "ownership": ownership_form,
                    "revenue": int(revenue),
                    "expenses": int(expenses),
                    "profit": profit
                })

                if profit > 0:
                    average_profit += profit

                firms_profit_dict[firm_name] = profit

    if len(firms_data) > 0:
        average_profit /= len(firms_data)

    result_list = [firms_profit_dict, {"average_profit": average_profit}]

    json_result = json.dumps(result_list, ensure_ascii=False, indent=2)
    with open("result.json", 'w', encoding='utf-8') as json_file:
        json_file.write(json_result)

    print("Список с прибылью и средней прибылью сохранён в result.json.")
    try:
        with open("result.json", 'r', encoding='utf-8') as json_file:
            result_data = json.load(json_file)

        print("Данные в result.json:")
        print(json.dumps(result_data, ensure_ascii=False, indent=2))
    except FileNotFoundError:
        print(f"Файл result.json не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении result.json: {e}")

except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
