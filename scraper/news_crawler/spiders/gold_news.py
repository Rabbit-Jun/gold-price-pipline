import scrapy


class GoldNewsSpider(scrapy.Spider):
    name = "gold_news"
    allowed_domains = []
    start_urls = ["https://www.google.com/search?sca_esv=f26a4e8abbd57b5a&rlz=1C1CHZN_enKR1141KR1142&q=%EA%B8%88%EA%B0%92&tbm=nws&source=lnms&fbs=AIIjpHyDg0Pef0CibV20xjIa-FReIKmAxsMTxuQCKLhb9OUJki0DxYQJ2cWp-4Nzr6A22He1IKbQbeHusnfe1kqhyqNHx5CQN_aqpnRMR3CU9P0zSU-_uxYMp_SdvAqm4SGs_ObaLQZ4SuREUs9e74R9GsZEhlj1uDVaEiuceIdQI1T3paahir14VXrwQXsdqGM9ldtl-LlHIJhA-_ZvF8fk_5nEA5JnudwQ2xDyOcsxNXiIpWVQCao&sa=X&ved=2ahUKEwju_6255OSRAxU8UPUHHe8SESwQ0pQJegQIFRAB&biw=871&bih=827&dpr=1.1"]

    def parse(self, response):
        print("====================================")
        articles= response.css('div.SoaBEf')

        for article in articles:
            title = article.css('div.n0jPhd::text').get()
            link = article.css('a.WlydOe::attr(href)').get()
            date = article.css('div.OSrXXb span::text').get()
            yield {
                'title': title,
                'link': link,
                'date': date
            }
            
