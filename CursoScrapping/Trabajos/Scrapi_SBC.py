from scrapy.item import Field
from scrapy.item import Item
from scrapy.loader.processors import MapCompose
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Contenido(Item):
    titulo=Field()
    ubicacion=Field()
    direccion=Field()
    precio=Field()
    date=Field()
    organizador=Field()

class eventbrite(CrawlSpider):
    name = "eventbriteSpider"
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        # 'FEED_EXPORT_ENCODING': 'utf-8'
    }
    # dominios alternos
    allowed_domain=['eventbrite.com.mx']
    # url semilla
    start_urls = ['https://www.eventbrite.com.mx/d/ecuador/events']
    # retardo de busqueda //util para no ser identificado q estoy haciendo scrapping
    dowload_delay=1
    rules=(
        Rule(
            # Extraigo todos los links de mi url semilla
            LinkExtractor(
                allow=r'/e/'
            ),follow=True,callback='parse_eventos'
        ),
    )

    # def remplace (selt,texto):
    #     nuevo_texto=texto.replace('•','-')
    #     if len(nuevo_texto)==0:
    #         nuevo_texto='Online'
    #     return nuevo_texto
    def parse_eventos(self,response):
        sel=Selector(response)
        titulo=sel.xpath('//h1[@class="listing-hero-title"]/text()').get()
        ubicacion=response.xpath('//h2[@class="listing-map-card-title text-medium"]/text()').get()
        direccion=response.xpath('//p[@class="listing-map-card-street-address text-default"]/text()').get()
        precio=response.xpath('//div[@class="js-display-price"]/text()').get()
        date=response.xpath('//p[@class="js-date-time-first-line"]//text()').get()
        organizador=response.xpath('//a[@class="js-d-scroll-to listing-organizer-name text-default"]/text()').get()

        titulo=self.limpieza(titulo)
        ubicacion=self.limpieza(ubicacion)
        direccion=self.limpieza(direccion)
        precio=self.limpieza(precio)
        date=self.limpieza(date)
        organizador=self.limpieza(organizador)

        item=ItemLoader(Contenido(),sel)
        item.add_value('titulo',titulo)
        item.add_value('ubicacion',ubicacion)
        item.add_value('direccion',direccion)
        item.add_value('precio',precio)
        item.add_value('date',date)
        item.add_value('organizador',organizador)
        yield item.load_item()
    def limpieza(self,texto):
        if not texto:
            return 'Sin Texto'
        else:
            return texto.replace('\t','').replace('\n','').strip()
