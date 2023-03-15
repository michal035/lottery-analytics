import scrapy


class LottoSpider(scrapy.Spider):
    name = "lotto_all"

    #works fine with multipple - infull thing there might be some issues
    start_urls = [
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2020-06-06,10',
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2000-06-06,10'
    ]

    def parse(self, response):   
                                 
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
            
            print(list_of_numbers)
            print("\n")

            
            
            print("LOTTO PLUS NUMERY")

             
            numbers = div_with_the_other_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            
            print(f"{list_of_numbers}")
            print("\n")
        


            print("LOTTO SUPER SZANSA")        

            numbers = div_with_the_other_numbers_super.xpath("div")

            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            
            print(f"{list_of_numbers}")
            print("\n")



        print("ONE GONE")

        