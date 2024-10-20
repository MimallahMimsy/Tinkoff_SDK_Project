import pandas as pd
from tinkoff.invest import Client


class Get_instr:

    @staticmethod
    def dataframe_maker(token):
        with Client(token) as client:
            BondsData = client.instruments.bonds(instrument_status=1).instruments
            CurrenciesData = client.instruments.currencies(instrument_status=1).instruments
            SharesData = client.instruments.shares(instrument_status=1).instruments

            Bonds = pd.DataFrame([{
                'name': row.name,
                'ticker': row.ticker.lower(),
                'figi': row.figi
            } for row in BondsData])
            Bonds.to_csv('Bonds.csv', index=False)

            Currencies = pd.DataFrame([{
                'name': row.name,
                'ticker': row.ticker.lower(),
                'figi': row.figi
            } for row in CurrenciesData])
            Currencies.to_csv('Currencies.csv', index=False)

            Shares = pd.DataFrame([{
                'name': row.name,
                'ticker': row.ticker.lower(),
                'figi': row.figi
            } for row in SharesData])
            Shares.to_csv('Shares.csv', index=False)

    @staticmethod
    def dataframe_reader(instr):
        Data = pd.read_csv(instr + '.csv')
        return Data

    @staticmethod
    def figi_finder(Instr, ticker):
        Data = Get_instr.dataframe_reader(Instr)
        filtered_str = Data.loc[Data['ticker'] == ticker.lower()]
        return repr(filtered_str.figi.squeeze()).replace("'", "")
