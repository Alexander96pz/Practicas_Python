from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Pregunta(Item):
    id = Field()
    pregunta = Field()
    #descripcion = Field()


class StackoverflowSpider(Spider):
    name = "StackoverflowSpider"
    custom_settings = {
      'USER_AGENT':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    start_urls = ['https://stackoverflow.com/questions']

    def parse(self, response):
        sel = Selector(response)
        titulo_de_pagina = sel.xpath('//h1/text()').get()
        print(titulo_de_pagina, 'Esta aqui')
        lista_preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        id = 0
        for preguntas in lista_preguntas:
             item = ItemLoader(Pregunta(),preguntas)
             item.add_xpath('pregunta','.//h3/a/text()')
             item.add_value('id',id)
             id+=1
             yield item.load_item()
