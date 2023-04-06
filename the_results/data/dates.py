import pandas as pd 
from main import get_dates
from datetime import datetime


df = get_dates()
result_df = pd.DataFrame({"number":[], "avrage_time_between":[], "last_draw": []})


def counting(dates):

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

        return sum_of_days, (sum_of_days/num_of_times_that_num_got_picked), previos_date



for i in list(df["number"]):

    dates = df[df["number"] == i]
    dates = pd.DataFrame(((dates["info"].str.split(' ')).to_list())[0],columns = ["dates"])
    dates["dates"] = pd.to_datetime(dates["dates"], infer_datetime_format=True, utc=True, errors='ignore')

    dates = dates.sort_values("dates")

    res = counting(dates)
    print(f"Number: {i} {res}")

    last_draw = res[2].strftime('%Y-%m-%d')
    avg = round(res[1],2)

    res_df = pd.DataFrame({"number":[i], "avrage_time_between":[avg], "last_draw": [last_draw]})
    result_df = pd.concat([result_df,res_df])


def get_dates_results():
     return result_df

    



