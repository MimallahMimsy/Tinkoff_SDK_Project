from Get_instr import Get_instr as gi
from Get_data import Get_data as gd
from Get_analyse import Get_analyse as ga
import csv
import tinkoff.invest


def _token_read():
    try:
        with open('tokens.csv', mode='r', newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            token = ''
            for row in csvreader:
                token = row[1]
            return token
    except FileNotFoundError:
        print("Файл с токеном не найден, введите токен вручную:")
        token = input()
        return token


token = _token_read()


def _main():
    try:
        print("Введите тикер инструмента:")
        ticker = input()
        gi.dataframe_maker(token)
        figi = gi.figi_finder('Shares', ticker)
        ga.drow_candels(token, figi, gd.start_time(), gd.end_time())

    except ValueError:
        print("Введенная дата не соответствует формату")
        _main()
    except KeyError:
        print("Некорректный интервал свечей")
        _main()
    except tinkoff.invest.RequestError:
        print("Следуя указаниям для вашего кода ошибки исправьте запрос \n "
              "Коды ошибки и их расшифровка:\n"
              "50002 - Инструмент не найден. Укажите корректный тикер инструмента\n"
              "30012 - Дата конца интервала не может быть меньше даты начала\n"
              "30014 - Превышен максимальный период запроса для данного интервала свечи\n"
              "11001 - Не удалось подкючиться к серверу, проверьте подключение к сети Интернет\n"
              "40003 - Токен доступа не найден или не активен")
        _main()


_main()

