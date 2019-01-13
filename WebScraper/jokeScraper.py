import scrapy
from scrapy.crawler import CrawlerProcess
import random

class JokesSpider(scrapy.Spider):
    name = 'jokes'
    start_urls = [
        'https://www.rd.com/funny-stuff/short-jokes/'
    ]

    def parse(self, response):
        validJokes = []
        for joke in response.xpath(".//div[@class='listicle-page']/descendant::text()").extract():
            #print("joke1 =" + joke)
            if(joke not in ['\n', 'Nicole Fornabaio/rd.com ', 'Nicole Fornabaio/rd.com', '.', '. ']):
                if(joke.find("jokes") == -1):
                    validJokes.append("'" + joke + "'")
        filename = 'jokes.txt'
        randomJoke =  validJokes[random.randint(0, len(validJokes))]
        with open(filename, 'wb') as f:
            #f.write(randomJoke.encode())
            f.write("\n".join(validJokes).encode())

def main():
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    res = process.crawl(JokesSpider)
    res2 = process.start()

if __name__ == "__main__":
    main()