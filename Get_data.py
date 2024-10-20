from tinkoff.invest import Client
import pandas as pd
from tinkoff.invest.schemas import CandleInterval
from datetime import datetime


class Get_data:
    @staticmethod
    def start_time():
        print("Нужно указать временной отрезок, для которого хотите получить свечи. Указывается время по Гринвичу (UTC+0)\n"
              "Введите дату начала в формате ДД-ММ-ГГ ЧЧ:ММ")

        ot = datetime.strptime(input(), '%d-%m-%y %H:%M')
        return ot

    @staticmethod
    def end_time():
        print("Введите дату конца отрезка в формате ДД-ММ-ГГ ЧЧ:ММ")
        do = datetime.strptime(input(), '%d-%m-%y %H:%M')
        return do

    @staticmethod
    def choose_candle_interval():
        print("Выберете интервал свечей и введите выбранное число, по умолчанию интервал дневной:\n "
              "1) Месяц \n"
              "2) Неделя \n"
              "3) День \n"
              "4) Час \n"
              "5) 30 минут \n"
              "6) 5 минут \n")
        inp = int(input())
        if inp == 1:
            return CandleInterval.CANDLE_INTERVAL_MONTH
        elif inp == 2:
            return CandleInterval.CANDLE_INTERVAL_WEEK
        elif inp == 3:
            return CandleInterval.CANDLE_INTERVAL_DAY
        elif inp == 4:
            return CandleInterval.CANDLE_INTERVAL_HOUR
        elif inp == 5:
            return CandleInterval.CANDLE_INTERVAL_30_MIN
        elif inp == 6:
            return CandleInterval.CANDLE_INTERVAL_5_MIN
        else:
            return CandleInterval.CANDLE_INTERVAL_DAY

    @staticmethod
    def Get_candels(token, figi, ot, do):
        with Client(token) as client:
            CandlesData = client.market_data.get_candles(figi=figi,
                                                         from_=ot,
                                                         to=do,
                                                         interval=Get_data.choose_candle_interval()).candles
            Candles = pd.DataFrame([{
                'time': row.time,
                'volume': row.volume,
                'open': Get_data.coin(row.open),
                'close': Get_data.coin(row.close),
                'high': Get_data.coin(row.high),
                'low': Get_data.coin(row.low)
            } for row in CandlesData])
            return Candles

    @staticmethod
    def coin(coins):
        return coins.units + coins.nano / 1e9
