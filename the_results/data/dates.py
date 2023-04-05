import pandas as pd 
from main import get_dates
import datetime


df = get_dates()

dates = df[df["number"] == "1"]
dates = pd.DataFrame(((dates["info"].str.split(' ')).to_list())[0],columns = ["dates"])
dates["dates"] = pd.to_datetime(dates["dates"])

dates = dates.sort_values("dates")



def counting():

    sum_of_days = 0
    num_of_times_that_num_got_picked  = len(dates)
    previos_date = None

    for i in (dates["dates"].tolist()):
        
        if previos_date != None:
            num_of_days = (i - previos_date).days  
            
            sum_of_days += num_of_days
            #print(num_of_days)
        
        previos_date = i
       
    #print(f"Sum: {sum_of_days} avg time to get picked: {(sum_of_days/num_of_times_that_num_got_picked)}")

    return sum_of_days, (sum_of_days/num_of_times_that_num_got_picked)


counting()

