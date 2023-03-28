import pandas as pd 
import matplotlib.pyplot as plt
from main import data_for_further_processing


df = data_for_further_processing()[1]


df['number'] = df['number'].astype(str)
df = df.sort_values(by='occurences', ascending=False)


colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6']
plt.barh(df['number'], df['occurences'], color=colors)



plt.xlabel('number of occurences')
plt.ylabel('Numbers')
plt.title('How many times each number got pick')


plt.show()
