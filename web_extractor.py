import bs4
import requests

# Aplicamos .format para recorrer todas las paginas de la web, recorriendo el url con n paginas
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# Titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,51):

    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,"lxml")

    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    for libro in libros:

        # Verificar que tengan 4 o 5 Estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")):

            # Guardar titulo en una variable
            titulo_libro = libro.select("a")[1]["title"]

            # Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Mostrar los libros de 4 o 5 estrellas en consola

for t in titulos_rating_alto:
    print(t)



