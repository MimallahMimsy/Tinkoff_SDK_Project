# Tinkoff_SDK_Project
Работаем с Tinkoff Invest API через официальную SDK для python. Код позволяет запрашивать биржевые котировки российских акций (а также облигаций и валют) и строить японские свечи для выбранного временного интервала. Возможно получить данные не старше года.
Для работы с API нужен получить токен в личном кабинете https://www.tbank.ru/invest/settings/ . Токен записывается в файл tokens.csv в формате token1,$, где $-токен. В репозиторий уже загружен файл с созданным токеном с доступом "только чтение", после сдачи работы токен будет удален. После считки токена, код записывает все торгуемые инструменты в csv файлы с полями name, tiker, figi. Выбор конкретного инструмента осуществляется введением его общепринятого на российском рынке тикера. После этого вводятся начало и конец временного интервала, затем выбирается интревал для свечи (доступны интервалы: месяц, неделя, день, час, 30 минут, 5 минут). Далее в браузере открывается построенная свечная модель. Интерфейс консольный. 
Используемые библиотеки: tinkoff.invest, pandas, datetime, plotly, csv.
