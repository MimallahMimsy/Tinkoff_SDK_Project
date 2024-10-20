# Tinkoff_SDK_Project
Работаем с Tinkoff Invest API через официальную SDK для python. Код позволяет запрашивать биржевые котировки российских акций (а также облигаций и валют) и строить японские свечи для выбранного временного интервала. Возможно получить данные не старше года.
Для работы с API нужен получить токен в личном кабинете https://www.tbank.ru/invest/settings/ . Токен записывается в файл tokens.csv в формате token1,$, где $-токен. В репозиторий уже загружен файл с созданным токеном с доступом "только чтение", после сдачи работы токен будет удален. После считки токена, код записывает все торгуемые инструменты в csv файлы с полями name, tiker, figi. Выбор конкретного инструмента осуществляется введением его общепринятого на российском рынке тикера. После этого вводятся начало и конец временного интервала, затем выбирается интревал для свечи (доступны интервалы: месяц, неделя, день, час, 30 минут, 5 минут). Далее в браузере открывается построенная свечная модель. Интерфейс консольный. 
Используемые библиотеки: tinkoff.invest, pandas, datetime, plotly, csv.
# Структура:
- Get_instr. Метод dataframe_maker запрашивает и создает csv файлы со списком интрументов, dataframe_reader считывает эти файлы, figi_finder находит нужный figi по полученному тикеру.
- Get_data. Методы start_time и end_time запрашивают концы временного интервала, choose_candle_interval позволяет выбрать интервал свечи, Get_candels запрашивает свечи по полученным интервалам, coin пересчитывает кастомное значение цены.
- Get_analyse. Строит японские свечи по полученным данным.
- main. Вызывает методы выше, считывает токен, отлавливает ошибки.
