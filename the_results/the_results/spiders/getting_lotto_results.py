import scrapy


#xpath with all the results on the certain page - //*[@id="__layout"]/div/div[2]/div/div[3]/div/div[2]/div/div


class LottoSpider(scrapy.Spider):
    name = "lotto"

    #works fine with multipple - infull thing there might be some issues
    start_urls = [
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2000-06-06,10',
        'https://www.lotto.pl/lotto/wyniki-i-wygrane/date,2020-06-06,10'
    ]

    def parse(self, response):
        
        the_div = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div")
        the_divs = the_div.xpath("div")
        for div in the_divs:
            #div = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]")
            div_with_numbers = div.xpath("div[3]/div/div[2]/div/div[3]")
                                
            #half-full paths - interesting
            """
            first_element = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div")[0]

            second_element = response.xpath("//*[@id='__layout']/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div/p")[0]
            """


            time = div.xpath("div/div/div/p/text()").get()
            print(f"TIME: {time}")
            
            #not working just yet idek

            draw_number = div.xpath("div[3]/div/div[2]/div/div[2]/p[2]/text()").get()
            print(f"DRAW NUMBER: {draw_number}")

           

            #PATH for div with one number /div[3]/div/div[2]/div/div[3]/div[6] -  //*[@id="__layout"]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1] /div[3]/div/div[2]/div/div[3]/div[6]
            
            #first_num = div.xpath("div[3]/div/div[2]/div/div[3]/div/text()").get()
            
            #print(f"FIRST: {first_num}")
            # this works as well ig - ./div[3]/div/div[2]/div/div[3]/div[1]/text()
            # but this dosent /div[3]/div/div[2]/div/div[3]/div/text() idek 

            print("NUMBERS")

            numbers = div_with_numbers.xpath("div")
            
            list_of_numbers = []
            for number in numbers:
                nu = int((number.xpath("text()").get()).replace("\n",""))
                
                list_of_numbers.append(nu)
            
            print(list_of_numbers)
            print("\n")

        print("ONE GONE")

        



# response.xpath("//p[@class='result-item__name']/text()").getall()
# response.xpath("//div[@class='recent-result-item Lotto']").getall()
# //*[@id="__layout"]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div/p