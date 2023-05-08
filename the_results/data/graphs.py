import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from main import get_main
from dates import get_dates_results
from datetime import datetime


df2 = get_dates_results()

# This is basically so that numbers don't go on top of each other 
def offset_for_labeles(ax, offset= -16):
    #offset = -16  
    for i, label in enumerate(ax.get_xticklabels()):
    
        y = offset
        ax.text(i, y, label.get_text(), ha='center', va='bottom', fontsize=10)
        
        offset = - 16
        if i%2 == 1:
            d = 0
        else:
            d = 6

        offset += d
        
    ax.set_xticklabels([])



sub_df1 = df2[["number","average_time_between"]]

sns.set_style("darkgrid")  
ax = sns.barplot(x='number', y='average_time_between', data=sub_df1, palette='Blues_d') 
plt.title("On average how long it takes for number to be picked again")  
plt.xlabel("number", labelpad=16) 
plt.ylabel("Number of days")  

offset_for_labeles(ax,-10)
plt.savefig('the_results/graphs/average_number_od_days.png')

#plt.show()
plt.clf()



df = get_main()[1]
df['number'] = df['number'].astype(str)
df = df.sort_values(by='occurences', ascending=False)

sub_df3 = df[['number','occurences']]

sns.set_style("darkgrid")  
ax = sns.barplot(x='number', y='occurences', data=sub_df3, palette='Oranges_r') 
plt.xlabel('number of occurences', labelpad=16)
plt.ylabel('Numbers')
plt.title('How many times each number got pick')

#plt.xticks(rotation=90)
offset_for_labeles(ax)
plt.savefig('the_results/graphs/basic_graph_number_of_picks.png')
#plt.show()
plt.clf()



sub_df1 = df2[["number","days_since_the_last_draw"]]

sns.set_style('whitegrid')
sns.despine()
ax = sns.barplot(x='number', y='days_since_the_last_draw', data=sub_df1, palette='twilight', label="")
plt.title("The amount of days that have passed since a certain number was picked")
plt.xlabel("numbers",labelpad=16)
plt.ylabel("Number of days")


offset_for_labeles(ax)


plt.savefig('the_results/graphs/days_since_last_pick.png')
