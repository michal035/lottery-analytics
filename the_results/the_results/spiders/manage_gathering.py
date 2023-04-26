from . import getting_all_results
#from getting_all_results import to_be_called_from_other_file
from datetime import datetime
import calendar
from time import sleep


# THIS FILE SHOULDN'T be in this directory 

# This is an attempt to fix an issue with a website limiting my rates - it's not about IP address. 
# I have a proxy rotation system ready from one of my previous projects,it would fix the issue as well, but 
# I think it would be overkill in this case.

#So i guess I will try to get data in 'bursts' of 6 months


now = datetime.now()
date = now.strftime("%Y-%m-%d")
num_of_years = 10



def main(date,num_of_years):
    
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    year = int(date_obj.strftime("%Y"))

    getting_all_results.to_be_called_from_other_file(f"{year}-01-01", date)

    #Spider can't be run again until the previous instance is still running
    sleep(7)

    year -= 1
    num_days = calendar.monthrange(year, 12)[1]

    date = f"{year}-12-{num_days}"

    num_of_years -= 1

    if num_of_years != 0:
        main(date,num_of_years)



main(date,num_of_years)




