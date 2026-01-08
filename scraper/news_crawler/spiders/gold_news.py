import scrapy


class GoldNewsSpider(scrapy.Spider):
    name = "gold_news"
    allowed_domains = []
    start_urls = ["https://www.google.com/search?q=%EA%B8%88%EA%B0%92&sca_esv=f26a4e8abbd57b5a&rlz=1C1CHZN_enKR1141KR1142&tbm=nws&ei=AUFfab36F5Hr1e8Pt-mlgAk&start=0&sa=N&story=Gh8IjAEaGgoTc3RvcnlfbGFiZWxfcGFydGlhbBID6riIMi8KJcfl4_6RorD28gG_nM2em8DW6COjrOjKl8PPgw3QvaXorq6vkHwQjsqwqBAYBXICEAI&fcs=ABHuY3SskcHLMsP9iQz0wGn0XfN8SKI7DQ&ved=2ahUKEwj9_p2tm_uRAxWRdfUHHbd0CZA4ChDy0wN6BAgGEAQ&biw=1920&bih=911&dpr=1&aic=0"]

    def parse(self, response):
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
            
        next_page = response.css('a#pnnext::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)