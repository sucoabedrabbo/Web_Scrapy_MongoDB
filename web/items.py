# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Informacion pagina principal
    titulo = scrapy.Field()

    #Informacion dentro de cada item
    _id = scrapy.Field()
    descripcion = scrapy.Field()
    localizacion = scrapy.Field()
    jornada = scrapy.Field()
    tipo = scrapy.Field()
    salario = scrapy.Field()
    empresa = scrapy.Field()
    requerimientos = scrapy.Field()
    #fechaDeContratacion = scrapy.Field()
    #cantidadDeVacantes = scrapy.Field()
    #educaciónMinima = scrapy.Field()
    #experiencia = scrapy.Field()
    #edad = scrapy.Field()
    #viajar = scrapy.Field()
    #cambioResidencia = scrapy.Field()