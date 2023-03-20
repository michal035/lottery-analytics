def get_urls(starting_date,end_date):
    
    #starting_date = "2010-01-01"
    #end_date = "2023-01-01"

    y_s = int((starting_date.split("-"))[0])
    y_e = int((end_date.split("-"))[0])


    years = [i + y_s for i in range(y_e - y_s)]
    urls = []

    for year in years:
        for month in range(12):
            url = f"https://www.lotto.pl/lotto/wyniki-i-wygrane/date,{year}-{month+1}-01,15"
            urls.append(url)

    urls.append(f"https://www.lotto.pl/lotto/wyniki-i-wygrane/date,{y_e}-01-01,15")
    
    return urls


