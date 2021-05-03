import requests
from bs4 import BeautifulSoup
cabezera={
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
url = "https://stackoverflow.com/questions"
resp=requests.get(url,headers=cabezera)

soap=BeautifulSoup(resp.text)
contenedor_preguntas=soap.find(id='questions')
lista_preguntas=contenedor_preguntas.find_all(class_='excerpt')
for pregunta in lista_preguntas:
    print(pregunta.text.replace('\n','').strip())
    print()