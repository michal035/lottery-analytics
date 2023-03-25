import pandas as pd 
import matplotlib as plt
from main import data_for_further_processing


df = data_for_further_processing()[1]

df = df.sort_values(by="number")

#just a random test graph
df.plot(x=df.columns[0], y=df.columns[1], kind='line')


plt.pyplot.show()

