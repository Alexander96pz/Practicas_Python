import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
url = "https://www.wikipedia.org/"
resp = requests.get(url, headers=encabezado)
# print(resp.text)
parser = html.fromstring(resp.text)
# =====FORMA 1==========
# contenido = parser.get_element_by_id("js-link-box-en")
# print(contenido.text_content())
# =====FORMA 2==========//valor exacto
# contenido = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
# print(contenido)
# ====== Forma 3 =======//valor similar
# contenido=parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
# print(contenido)
# for idioma in contenido:
#     print(idioma)
# ======= Forma 4 =====
contenido = parser.find_class("central-featured-lang")
for idioma in contenido:
    print(idioma.text_content())
