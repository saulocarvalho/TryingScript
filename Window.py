import tkinter
import pandas_datareader 

#janela = tkinter.Tk()
#janela.title("Teste")

#janela.mainloop()

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

cotacao_bovespa = web.DataReader('^BVSP',data_source='yahoo', start="1/1/2020", end="1/1/2021")
display(cotacao_bovespa)