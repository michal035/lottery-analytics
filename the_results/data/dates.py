import pandas as pd 
from main import get_dates


df = get_dates()

dates = df[df["number"] == "1"]
dates = pd.DataFrame(((dates["info"].str.split(' ')).to_list())[0],columns = ["dates"])
dates["dates"] = pd.to_datetime(dates["dates"])

#dates["dates"] = dates["dates"].sort_values(inplace=True)


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