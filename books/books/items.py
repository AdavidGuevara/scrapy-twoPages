import scrapy


class BooksItem(scrapy.Item):
    nombre = scrapy.Field()
    precio = scrapy.Field()
    has_ebook = scrapy.Field()
