
# Publicar automáticamente los productos de Woocommerce en Instagram con Python

Conectando esta aplicación a tu tienda de Woocommerce y a la API de Instagram podrás publicar automáticamente presionando un sólo botón.


## Funcionamiento

Lo que hace la aplicación es conectarse a la tienda de Woocommerce a través de la Woo API Key y descarga la inmformación de todos los productos, luego al presionar el botón "Publicar", selecciona al azar un producto de la base de datos previamente cargada y publica en instagram el producto haciendo uso de la Instagram API key que obtienes en Facebook Developers.

La publicación relizada incluye la foto del producto (la misma foto de la tienda en línea) y la descripción o el "copy" de la publicación que lo obtiene de la inmformación alternativa de la imagen o el "ALT" ya que este campo de texto permite agregar hashtags y emojis sin alterar el campo con etiquetas HTML.
## Funcionalidades

- Light/dark mode toggle
- Permite actualizar la Instagram API Key
- Descarga de base de datos de Woocommerce
- Publicación en Instagram con un solo click

## Instalación

Las librerias de Python requeridas son:
Pyllow, woocommerce, Requests y Customtkinter.
(Escribe los siguientes comandos por separado en el CMD (Símbolo del sistema) de Windows.)

```bash
  pip install pil
  pip install woocommerce
  pip install requests
  pip install customtkinter
```

Usa un editor de código para ejecutar el script de Python y para personalizar los campos, esto último es opcional.
Al finalizar la personalización de los campos puedes crear un ejecutable con la librería Auto-py-to-exe.

```bash
pip install auto-py-to-exe
```
## Relacionado

Puedes ver el video de Youtube donde se explica a detalle sobre este proyecto.

[![youtube](https://img.shields.io/badge/youtube-f21d1d?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@codeffee_)



## Screenshots

![App Screenshot](https://elsalvadorvisit.com/blog-img/playa-el-zonte-la-libertad-2.jpg)


