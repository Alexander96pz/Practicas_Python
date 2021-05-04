from scrapy import Item,Field,Spider,Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
#Estructura
class Contenido(Item):
    id = Field()
    # descripcion=Field()
#Configuracion
class UniversalSpider(Spider):
    name = "Universal_Spider"
    custom_settings = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    start_urls=['https://www.eluniverso.com/deportes/']
    #metodo obtencion del dato//parseado
    def parse(self, response):
        # sel=Selector(response) # similares
        soup=BeautifulSoup(response.body)

        # lista_contenido=sel.xpath('//div[@class="region region-content | col-span-12 sm:col-span-12 lg:col-span-8 grid grid-cols-12 col-gap-2  lg:border-r lg:pr-4  auto-rows-max"]//li[@class="relative"]')
        # contenido_p=soup.find('div',class_='region region-content | col-span-12 sm:col-span-12 lg:col-span-8 grid grid-cols-12 col-gap-2  lg:border-r lg:pr-4  auto-rows-max')
        # contenido_p = soup.find_all('p',class_="table m-auto px-2 pb-2 bg-white text-center border border-grey-100 text-xs")
        # if(contenido_p !=)

        # lista_contenido=soup.find_all('li',class_='relative')
        # print(contenido_p)
        # for contenido in lista_contenido:
        #     item=ItemLoader(Contenido(),response.body)
        # #     item.add_xpath('id','.//div[@class="card-content | space-y-1"]/h2/a/text()')
        #     card_content=contenido.find('div',class_="card-content | space-y-1")
        #     h2=card_content.find('h2',class_="text-base m-0 font-bold font-primary")
        #     id=h2.find('a').text
        #     yield item.load_item()