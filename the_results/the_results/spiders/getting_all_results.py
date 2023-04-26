import scrapy
from scrapy import Request
import pandas as pd

# This is a workaround for the inconsistency of Python's relative imports, which can sometimes fail

try:
    from . import urls
except:
    import urls


#This is the same what lotto_r.py is - this file is made to be run from bash script (just like any .py file would be) 
# not via consle aka 'scrapy shell'


class LottoSpider(scrapy.Spider):
    
    name = "lotto_all"

    results_df = pd.DataFrame({ 'date': [], 'lotto': [], 'lotto-plus': [], 'super-szansa': []})
    results_df.to_csv("the_results/re3.csv", index=None, sep=';', mode='w')


    def __init__(self, *args, **kwargs):
        super(LottoSpider, self).__init__(*args, **kwargs)
        self.arg1 = kwargs.get('arg1')
        self.arg2 = kwargs.get('arg2')

        #this returns urls from that range of dates 
        self.start_urls = urls.get_urls(self.arg1,self.arg2)

        #just for troubleshooting 
        #print(f"URLS! {self.start_urls}")
    

    def start_requests(self):
        

        counter = 0
        for url in self.start_urls:
            print(url)
            counter += 1
            print(f"COUNTER:   {counter}")


            """headers =  {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.eventscribe.com', #need to test if removing this would do anything
            'Referer': url, 
            "user_agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'X-Requested-With': 'XMLHttpsRequest'
            }"""


            #re =  Request(url=url, callback=self.parse)
            #scrapy.http.Request(url, method='GET',  dont_filter=True)   
            #headers=headers
            yield Request(url=url, callback=self.parse)


    def parse(self, response):   
        global results_df

        the_div = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div")
        the_divs = the_div.xpath("div")
        
        for div in the_divs:
            div_with_the_other_numbers = div.xpath("div[3]/div/div[3]/div/div[3]")
            div_with_the_other_numbers_super = div.xpath("div[3]/div/div[4]/div/div[3]")
            div_with_numbers = div.xpath("div[3]/div/div[2]/div/div[3]")
                                


            time = div.xpath("div/div/div/p/text()").get()
            #print(f"TIME: {time}")
 
            draw_number = div.xpath("div[3]/div/div[2]/div/div[2]/p[2]/text()").get()
            #print(f"DRAW NUMBER LOTTO: {draw_number}")

            #print("NUMBERS_LOTTO")

            numbers = div_with_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                lotto_numbers = ' '.join(str(i) for i in list_of_numbers)
            else:
                lotto_numbers = 'NaN'

            #print(list_of_numbers)
            #print("\n")

            
            
            #print("LOTTO PLUS NUMERY")

             
            numbers = div_with_the_other_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                lotto_numbers_plus = ' '.join(str(i) for i in list_of_numbers)
            else:
                lotto_numbers_plus = "NaN"
                
            #print(f"{list_of_numbers}")
            #print("\n")
        


            #print("LOTTO SUPER SZANSA")        

            numbers = div_with_the_other_numbers_super.xpath("div")

            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            

            if len(list_of_numbers) != 0:
                super_numbers = ' '.join(str(i) for i in list_of_numbers)
            else:
                super_numbers = "NaN"

            #print(f"{list_of_numbers}")
            #print("\n")



            if time != None:
                time = (str(time).replace(" ","")).replace("\n","")
            else: 
                time = "NaN"

            df = pd.DataFrame({ 'date': [time], 'lotto': [lotto_numbers], 'lotto-plus': [lotto_numbers_plus], 'super-szansa': [super_numbers]}, index=[0])
            df.to_csv("the_results/re3.csv",index=None,header=None, sep=';', mode='a')

        #print("ONE GONE")



def to_be_called_from_other_file(date1,date2):
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={
        "FEEDS": {
            "ritems3.json": {"format": "json"},
        },
    })


    process.crawl(LottoSpider, arg1 = date1,arg2 = date2)
    process.start() 


