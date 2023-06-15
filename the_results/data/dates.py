import pandas as pd 
from main import get_dates
from datetime import datetime
import pytz


df = get_dates()
result_df = pd.DataFrame({"number":[], "average_time_between":[], "last_draw": []})


now = datetime.now(pytz.UTC)

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
    dates["dates"] = pd.to_datetime(dates["dates"], infer_datetime_format=True, utc=True, errors='ignore', dayfirst=True)

    dates = dates.sort_values("dates")
    res = counting(dates)
        
    #print(f"Number: {i} {res}")

    prev_date = res[2]

    
    new_prev_date_string = prev_date.strftime('%d-%m-%Y')
    prev_date = pytz.utc.localize(pd.to_datetime(new_prev_date_string, dayfirst=True))


    last_draw = res[2].strftime('%Y-%m-%d')
    avg = round(res[1],2)
    time_since_last_draw = (now - prev_date).days

   """
   if time_since_last_draw < 0:
         print("here")
         print(time_since_last_draw)
         print(f"{now} {prev_date}")
         print(type(prev_date))
   """

    res_df = pd.DataFrame({"number":[i], "average_time_between":[avg], "last_draw": [last_draw], "days_since_the_last_draw": [time_since_last_draw]})
    result_df = pd.concat([result_df,res_df])


def get_dates_results():
     return result_df

    



