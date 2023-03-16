import scrapy
import pandas as pd



class LottoSpider(scrapy.Spider):
    
    name = "lotto_all"


    start_urls = [
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2020-06-06,10',
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2000-06-06,10'
    ]

    results_df = pd.DataFrame({ 'date': [], 'lotto': [], 'lotto-plus': [], 'super-szansa': []})
    def parse(self, response):   
        global results_df

        the_div = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div")
        the_divs = the_div.xpath("div")
        
        for div in the_divs:
            div_with_the_other_numbers = div.xpath("div[3]/div/div[3]/div/div[3]")
            div_with_the_other_numbers_super = div.xpath("div[3]/div/div[4]/div/div[3]")
            div_with_numbers = div.xpath("div[3]/div/div[2]/div/div[3]")
                                


            time = div.xpath("div/div/div/p/text()").get()
            print(f"TIME: {time}")

            draw_number = div.xpath("div[3]/div/div[2]/div/div[2]/p[2]/text()").get()
            print(f"DRAW NUMBER LOTTO: {draw_number}")

            print("NUMBERS_LOTTO")

            numbers = div_with_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                lotto_numbers = ' '.join(str(i) for i in list_of_numbers)
            else:
                lotto_numbers = 'NaN'

            print(list_of_numbers)
            print("\n")

            
            
            print("LOTTO PLUS NUMERY")

             
            numbers = div_with_the_other_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                lotto_numbers_plus = ' '.join(str(i) for i in list_of_numbers)
            else:
                lotto_numbers_plus = "NaN"
                
            print(f"{list_of_numbers}")
            print("\n")
        


            print("LOTTO SUPER SZANSA")        

            numbers = div_with_the_other_numbers_super.xpath("div")

            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                super_numbers = ' '.join(str(i) for i in list_of_numbers)
            else:
                super_numbers = "NaN"

            print(f"{list_of_numbers}")
            print("\n")


            print(lotto_numbers)
            df = pd.DataFrame({ 'date': time, 'lotto': lotto_numbers, 'lotto-plus': lotto_numbers_plus, 'super-szansa': super_numbers}, index=[0])
            results_df = pd.merge(results_df,df)
            print(results_df)


        print("ONE GONE")
        print(results_df)

        