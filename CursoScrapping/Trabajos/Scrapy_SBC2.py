from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Contenido(Item):
    id = Field()
    titulo=Field()
    # tipo_evento=Field()
    hora_evento=Field()
    lugar_evento=Field()
    # date=Field()
    # price=Field()


class eventbrite(Spider):
    name = "googleEventSpider"
    custom_settings = {
      'USER_AGENT':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    start_urls = ['https://www.google.com/search?q=eventos+culturales+ecuador&oq=eventos+Culturales+ecuador&aqs=chrome.0.69i59j0i22i30l3j69i60.8319j0j7&sourceid=chrome&ie=UTF-8&ibp=htl;events&rciv=evn&sa=X&ved=2ahUKEwis0Mja1qzwAhVOFVkFHReqBeMQ5rwDKAJ6BAgFEA0#htivrt=events&htidocid=L2F1dGhvcml0eS9ob3Jpem9uL2NsdXN0ZXJlZF9ldmVudC8yMDIxLTA0LTI5fDExMjk5MDQwNDAxMjUzODMwNzA0&fpstate=tldetail']

    def parse(self, response):
        sel = Selector(response)
        lista_eventos = sel.xpath('//div[@class="K9YWpe"]//li["PPaEvOc tv5olb gws-horizon-textlists__li-ed"]')
        id = 0
        for evento in lista_eventos:
             item = ItemLoader(Contenido(),evento)
             item.add_value('id', id)
             item.add_xpath('titulo','.//div[@class="YOGjf"]/text()')
             item.add_xpath('hora_evento', './/div[@class="cEZxRc"]/text()')
             item.add_xpath('lugar_evento', './/div[@class="cEZxRc zvDXNd"]/text()')
             id+=1
             yield item.load_item()