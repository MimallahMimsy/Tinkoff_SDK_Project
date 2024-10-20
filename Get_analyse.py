from Get_data import Get_data as gd
import plotly.graph_objects as go



class Get_analyse:
    @staticmethod
    def drow_candels(token, figi, ot, do):
        Data = gd.Get_candels(
            token,
            figi,
            ot,
            do)
        fig = go.Figure(data=[go.Candlestick(x=Data['time'],
                                             open=Data['open'],
                                             high=Data['high'],
                                             low=Data['low'],
                                             close=Data['close'])])
        fig.show()
