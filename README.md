# Web Scraper de Libros con Calificación Alta

Este script en Python utiliza las bibliotecas `requests` y `BeautifulSoup4` para extraer los títulos de los libros con calificaciones de 4 o 5 estrellas del sitio web [Books to Scrape](https://books.toscrape.com/).

## Descripción

El script realiza las siguientes acciones:

1.  **Importa las bibliotecas necesarias:**
    *   `bs4` (BeautifulSoup4) para el análisis HTML.
    *   `requests` para realizar solicitudes HTTP a la web.

2.  **Define la URL base:** Utiliza la función `.format()` para construir las URLs de cada página de resultados en el sitio web.

3.  **Inicializa la lista `titulos_rating_alto`:** Esta lista almacenará los títulos de los libros que cumplan con el criterio de calificación alta.

4.  **Itera a través de 50 páginas:** Recorre las 50 páginas de resultados del sitio web.
    *   Construye la URL específica de la página.
    *   Realiza una petición `GET` a la URL para obtener el contenido HTML de la página.
    *   Crea un objeto `BeautifulSoup` para parsear el HTML.
    *   Selecciona todos los elementos HTML con la clase `product_pod` (que contienen la información de cada libro).

5.  **Itera a través de los libros de cada página:**
    *   Verifica si el libro tiene una calificación de 4 o 5 estrellas usando los selectores de clase CSS `.star-rating.Four` y `.star-rating.Five`.
    *   Si el libro tiene la calificación buscada:
        *   Extrae el título del libro del atributo `title` del segundo enlace (`<a>`) dentro del elemento `product_pod`.
        *   Agrega el título a la lista `titulos_rating_alto`.

6.  **Imprime los títulos de los libros:** Después de iterar todas las páginas, imprime en la consola cada uno de los títulos almacenados en la lista `titulos_rating_alto`.

## Requisitos

*   Python 3.6 o superior.
*   Las bibliotecas `requests` y `BeautifulSoup4`. Puedes instalarlas usando pip:

    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1.  Clona o descarga este repositorio a tu máquina.
2.  Asegúrate de tener instalado Python y las bibliotecas necesarias.
3.  Ejecuta el script `web_extractor.py`
    ```bash
    python main.py
    ```
4.  El script imprimirá en la consola la lista de títulos de los libros con 4 o 5 estrellas de las 50 páginas del sitio web.

## Advertencias

*   Este script está diseñado para el sitio web específico [Books to Scrape](https://books.toscrape.com/). Cambios en la estructura HTML del sitio pueden causar que el script deje de funcionar correctamente.
*   Es importante ser respetuoso con el sitio web al hacer scraping. Evita realizar demasiadas peticiones en un corto período de tiempo para no sobrecargar el servidor. Considera implementar retardos o ajustes en el script si lo ejecutas con frecuencia.
