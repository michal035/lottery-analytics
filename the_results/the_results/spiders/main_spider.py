import scrapy

class LottoSpider(scrapy.Spider):
    name = "lotto"
    start_urls = [
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2000-06-06,10',
    ]

    def parse(self, response):
        
        div = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]")
        div_with_numbers = div.xpath("div[3]/div/div[2]/div/div[3]")
                             
        #half-full paths - interesting
        """
         first_element = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div")[0]

        second_element = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div/p")[0]
        """

        time = div.xpath("div/div/div/p/text()").get()
        print(f"TIME: {time}")


        #PATH for div with one number /div[3]/div/div[2]/div/div[3]/div[6] -  //*[@id="__layout"]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1] /div[3]/div/div[2]/div/div[3]/div[6]
        first_num = div.xpath("div[3]/div/div[2]/div/div[3]/div/text()").get()
        print(f"FIRST: {first_num}")
        # this works as well ig - ./div[3]/div/div[2]/div/div[3]/div[1]/text()
        # but this dosent /div[3]/div/div[2]/div/div[3]/div/text() idek 

        print("NUMBERS")

        numbers = div_with_numbers.xpath("div")
        for number in numbers:
            nu = number.xpath("text()").get()
            print(nu)

        

        



# response.xpath("//p[@class='result-item__name']/text()").getall()
# response.xpath("//div[@class='recent-result-item Lotto']").getall()
# //*[@id="__layout"]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div/p