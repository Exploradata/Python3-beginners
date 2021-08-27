
from bs4 import BeautifulSoup
import urllib.request

# Petición/lectura
url = 'https://es.wikipedia.org/wiki/Web_scraping'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Título del sitio en formato str
title = soup.find(id = 'firstHeading')

print('Título del sitio:', soup.title.string)
print('Artículo:', title.string, '\n')

# Número de enlaces
count = 0
# Tipo de etiqueta
tag = soup('a', href= True)
# Filtro para https, tags y slugs
indx = 'h'

urls = []
for link in tag:
    link = link.get('href')
    # Filtro indx según primer caracter
    if link[0] == indx:
        urls.append(link)
        count += 1
        
# Imprimimos todas las urls
for url in urls:
    if url.startswith('http'):
        print('URL:', url)
    elif url.startswith('/'):
        print('SLUG:', url)
    else:
        print('TAG:', url)
