import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from main import get_main
from dates import get_dates_results



df2 = get_dates_results()
sub_df1 = df2[["number","avrage_time_between"]]



sns.set_style("darkgrid")  
sns.barplot(x='number', y='avrage_time_between', data=sub_df1, palette='Blues_d') 
plt.title("On avarge how long it takes for number to be picked again")  
plt.xlabel("number") 
plt.ylabel("Number of days")  
plt.show()


#just some basic graph showing how many times each number occured 
"""df = get_main()[1]


df['number'] = df['number'].astype(str)
df = df.sort_values(by='occurences', ascending=False)


colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6']
plt.barh(df['number'], df['occurences'], color=colors)



plt.xlabel('number of occurences')
plt.ylabel('Numbers')
plt.title('How many times each number got pick')
"""

#plt.show()


