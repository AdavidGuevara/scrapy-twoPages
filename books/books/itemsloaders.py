from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class BookLoader(ItemLoader):
    default_output_processor = TakeFirst()
    nombre_in = MapCompose(lambda x: x.lower())
    precio_in = MapCompose(lambda x: x.split("£")[-1])
