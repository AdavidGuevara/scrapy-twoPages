from ..itemsloaders import BookLoader
from ..items import BooksItem
import scrapy


class GutembergSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com", "gutenberg.org"]

    def start_requests(self):
        url = "https://books.toscrape.com/catalogue/page-{}.html"
        for i in range(1, 51):
            yield scrapy.Request(url=url.format(i))

    def parse(self, response):
        for article in response.xpath("//article"):
            item = {
                "precio": article.xpath('.//p[@class="price_color"]/text()').get(),
                "nombre": article.xpath(".//h3/a/@title").get(),
            }

            url = (
                "https://www.gutenberg.org/ebooks/search/?query={}&submit_search=Go%21"
            )
            yield scrapy.Request(
                url=url.format(item["nombre"]),
                callback=self.parse_gutenberg,
                cb_kwargs={"item": item},
            )

    def parse_gutenberg(self, response, item):
        has_ebook = False
        result = response.xpath(
            '//span[contains(text(),"Displaying results")]/text()'
        ).get()
        if result:
            has_ebook = True

        book = BookLoader(BooksItem(), response)
        book.add_value("nombre", item["nombre"])
        book.add_value("precio", item["precio"])
        book.add_value("has_ebook", has_ebook)
        yield book.load_item()
