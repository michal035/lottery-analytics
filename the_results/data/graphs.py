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


plt.savefig('the_results/graphs/average_number_od_days.png')
#plt.show()
plt.clf()



df = get_main()[1]
df['number'] = df['number'].astype(str)
df = df.sort_values(by='occurences', ascending=False)

sub_df3 = df[['number','occurences']]

sns.set_style("darkgrid")  
sns.barplot(x='number', y='occurences', data=sub_df3, palette='Oranges_r') 
plt.xlabel('number of occurences')
plt.ylabel('Numbers')
plt.title('How many times each number got pick')


plt.savefig('the_results/graphs/basic_graph_number_of_picks.png')
#plt.show()
plt.clf()



sub_df1 = df2[["number","days_since_the_last_draw"]]

sns.set_style('whitegrid')
sns.despine()
sns.barplot(x='number', y='days_since_the_last_draw', data=sub_df1, palette='twilight') 
plt.title("The amount of days that have passed since a certain number was picked")  
plt.xlabel("number") 
plt.ylabel("Number of days")  


plt.savefig('the_results/graphs/days_since_last_pick.png')
#plt.show()