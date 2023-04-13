import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from main import get_main
from dates import get_dates_results
from datetime import datetime



df2 = get_dates_results()
sub_df1 = df2[["number","avrage_time_between"]]



sns.set_style("darkgrid")  
sns.barplot(x='number', y='avrage_time_between', data=sub_df1, palette='Blues_d') 
plt.title("On avarge how long it takes for number to be picked again")  
plt.xlabel("number") 
plt.ylabel("Number of days")  

# plt.show()
plt.savefig('the_results/graphs/average_number_od_days.png')

#just some basic graph showing how many times each number occured 
df = get_main()[1]
plt.clf()

df['number'] = df['number'].astype(str)
df = df.sort_values(by='occurences', ascending=False)


colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6']
plt.barh(df['number'], df['occurences'], color=colors)



plt.xlabel('number of occurences')
plt.ylabel('Numbers')
plt.title('How many times each number got pick')


#plt.show()
plt.savefig('the_results/graphs/basic_graph_number_of_picks.png')
plt.clf()



sub_df1 = df2[["number","days_since_the_last_draw"]]

sns.set_style('whitegrid')
sns.despine()
sns.barplot(x='number', y='days_since_the_last_draw', data=sub_df1, palette='Blues_d') 
plt.title("On avarge how long it takes for number to be picked again")  
plt.xlabel("number") 
plt.ylabel("Number of days")  

plt.show()
plt.savefig('the_results/graphs/days_since_last_pick.png')
