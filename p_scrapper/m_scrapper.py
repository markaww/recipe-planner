import bs4
import requests
import re
import pandas as pd

# Make a list of all the category pages contained in the website

cats = ['https://www.recetasgratis.net/Recetas-de-Arroces-cereales-listado_receta-9_',
        'https://www.recetasgratis.net/Recetas-de-Aves-caza-listado_receta-11_',
        'https://www.recetasgratis.net/Recetas-de-Carne-listado_receta-10_',
        'https://www.recetasgratis.net/Recetas-de-Ensaladas-listado_receta-4_',
        'https://www.recetasgratis.net/Recetas-de-Legumbres-listado_receta-8_',
        'https://www.recetasgratis.net/Recetas-de-Pasta-listado_receta-5_',
        'https://www.recetasgratis.net/Recetas-de-Pescado-listado_receta-12_',
        'https://www.recetasgratis.net/Recetas-de-Sopa-listado_receta-6_',
        'https://www.recetasgratis.net/Recetas-de-Verduras-listado_receta-7_']

pages = [str(i) for i in range(1,51)]
catpages_long = [(cat + page + '.html') for cat in cats for page in pages]

catpages_short = []
for i in catpages_long:
    if len(requests.get(i).history) == 0:
        catpages_short.append(i)
    elif len(requests.get(i).history) > 0:
        pass

# Iterating through all the category pages, fetch individual recipe URLs

recipe_urls = []
for page in catpages_short:
    r = requests.get(page)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    recipe = soup.find_all('a', attrs={'class': 'titulo titulo--resultado'})
    for i in list(range(0,len(recipe))):
        recipe_urls.append(recipe[i]['href'])

recipe_url_list = []
name_list = []
categoria_list = []
comensales_list = []
duracion_list = []
plato_list = []
dificultad_list = []
caracteristicas_list = []
ingredientes_list = []

# Using the list of 10k recipe URLs, scrape specific features for each recipe

for url in recipe_urls:
        soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
        recipe = soup.find_all('div', attrs={'class': 'recipe-info'})

        try:
                recipe_url_list.append(requests.get(url).url)
        except:
                recipe_url_list.append('NaN')

        try:
                name_list.append(soup.find_all('h1', attrs={'class': 'titulo titulo--articulo'})[0].text[10:])
        except:
                name_list.append('NaN')

        try:
                categoria_list.append(
                        re.findall('(^.+?)\\n', (soup.find_all('ul', attrs={'class': 'breadcrumb'}))[0].text[9:])[0])
        except:
                categoria_list.append('NaN')

        try:
                comensales_list.append(recipe[0].find('span', attrs={'class': 'property comensales'}).text[:-11])
        except:
                comensales_list.append('NaN')

        try:
                duracion_list.append(recipe[0].find('span', attrs={'class': 'property duracion'}).text)
        except:
                duracion_list.append('NaN')

        try:
                plato_list.append(recipe[0].find('span', attrs={'class': 'property para'}).text)
        except:
                plato_list.append('NaN')

        try:
                dificultad_list.append(recipe[0].find('span', attrs={'class': 'property dificultad'}).text)
        except:
                dificultad_list.append('NaN')

        try:
                caracteristicas_list.append((recipe[0].find('div', attrs={'class': 'properties inline'}).text)[30:])
        except:
                caracteristicas_list.append('NaN')

        try:
                ingredientes_list.append(
                        ', '.join(recipe[0].find('div', attrs={'class': 'ingredientes'}).text.split('\n\n\n\n\n'))[
                        2:].replace('\n', ''))
        except:
                ingredientes_list.append('NaN')

# Create a table with the resulting features

recipe_dict = {
        'URL': recipe_url_list,
        'Nombre': name_list,
        'Categoria': categoria_list,
        'Comensales': comensales_list,
        'Tiempo': duracion_list,
        'Tipo': plato_list,
        'Dificultad': dificultad_list,
        'Caracteristicas': caracteristicas_list,
        'Ingredientes': ingredientes_list,
}

recipes = pd.DataFrame(recipe_dict)