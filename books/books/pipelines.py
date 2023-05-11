from itemadapter import ItemAdapter


class BooksPipeline:
    def process_item(self, item, spider):
        return item


class PriceToUSDPipeline:
    gbpToUsdRate = 1.26

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get("precio"):
            precioFloat = float(adapter["precio"])
            adapter["precio"] = precioFloat * self.gbpToUsdRate
            return item
