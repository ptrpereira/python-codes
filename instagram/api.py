import urllib.request
import re
import time
pagina1 = urllib.request.urlopen(
        'https://instagram.com/explore/tags/hashtag1')
texto1 = pagina1.read().decode('utf8')
link_list = re.findall('thumbnail_resources', texto1)
count = len(link_list)
onde = texto1.find('thumbnail_resources":[{"src":"')
lista_post = texto1.split('thumbnail_resources":[{"src":"')
links = []
for i in range(1, count):
    onde_inicio = lista_post[i].find('thumbnail_resources":[{"src":"')
    inicio = onde_inicio + 1
    onde_fim = lista_post[i].find('?_nc_ht=instagram.fplu8-1.fna.fbcdn.net')
    fim = onde_fim + 39
    if lista_post[i] not in links:
        links.append(lista_post[i][inicio:fim])
lista_links1 = list(dict.fromkeys(links))
# Lista2
pagina2 = urllib.request.urlopen(
        'https://instagram.com/explore/tags/hashtag2')
texto2 = pagina2.read().decode('utf8')
link_list = re.findall('thumbnail_resources', texto2)
count = len(link_list)
onde = texto2.find('thumbnail_resources":[{"src":"')
lista_post = texto2.split('thumbnail_resources":[{"src":"')
links = []
for i in range(1, count):
    onde_inicio = lista_post[i].find('thumbnail_resources":[{"src":"')
    inicio = onde_inicio + 1
    onde_fim = lista_post[i].find('?_nc_ht=instagram.fplu8-1.fna.fbcdn.net')
    fim = onde_fim + 39
    if lista_post[i] not in links:
        links.append(lista_post[i][inicio:fim])
lista_links2 = list(dict.fromkeys(links))

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 


total = (intersection(lista_links1, lista_links2))

# Arquivo
arquivo = open('lista.js', 'w')
arquivo.write('const arr = {}'.format(total))
arquivo.close()
