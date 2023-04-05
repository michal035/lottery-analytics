import pandas as pd 
from main import get_dates
import datetime


df = get_dates()

dates = df[df["number"] == "1"]
dates = pd.DataFrame(((dates["info"].str.split(' ')).to_list())[0],columns = ["dates"])
dates["dates"] = pd.to_datetime(dates["dates"])

dates = dates.sort_values("dates")


def counting():

    o_year = 0
    counter = 0
    sum_od_days = 0
    previos_date = None

    for i in (dates["dates"].tolist()):
        
        if previos_date != None:
            num_of_days = (i - previos_date).days  
            print(num_of_days)
        
        previos_date = i
       
                


counting()

#print(dates.iloc[2,0])



"""
years_for_certain_num = pd.DataFrame()

cur_y = ""

for i in dates[0]:
    if (temp_y := (i.split("."))[2]) != cur_y:
        cur_y = temp_y
       """ 

"""for i in df["number"]:
    print(df["info"][df["number"]==i])
"""