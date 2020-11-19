import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from web.items import WebItem

class web(CrawlSpider):
    name= 'web'
    item_count = 0
    allowed_domain= ['https://www.computrabajo.com.ec/']
    start_urls = ['https://www.computrabajo.com.ec/ofertas-de-trabajo/?p=1']

    rules = {
        Rule(LinkExtractor(allow =(),restrict_xpaths =  ('//li[@class="siguiente"]/a'))), #Regla para la siguiente pagina
        Rule(LinkExtractor(allow =(),restrict_xpaths =  ('//h2')),callback= 'parse_item',follow = False) #Regla para que entre en cada trabajo
    }

    def parse_item (self,response):
        web_item = WebItem()
        dic = {} # diccionario de informacion de requerimientos
        #importamos la informacion

        web_item['titulo']  = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/header/h1/text())').extract_first()
        web_item['empresa'] = response.xpath('normalize-space(//*[@id="urlverofertas"])').extract()[0]
        web_item['descripcion'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[2])').extract()[0]

        for index in range(3,10):
            cadena = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[{}])'.format(index)).extract()
            frase = cadena[0].split(':')
            if len(frase) == 2:
                dic[frase[0]] = frase[1]

        web_item['requerimientos'] = dic

        #web_item['fechaDeContratacion'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[3])').extract()
        #web_item['cantidadDeVacantes'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[4])').extract()
        web_item['localizacion'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[4]/ul/li[3]/p)').extract()[0]
        web_item['jornada'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[4]/ul/li[4]/p)').extract()[0]
        web_item['tipo'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[4]/ul/li[5]/p)').extract()[0]
        web_item['salario'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[4]/ul/li[6]/p)').extract()[0]
        #web_item['educaciónMinima'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[5])').extract()
        #web_item['experiencia'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[6])').extract()
        #web_item['edad'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[7])').extract()
        #web_item['viajar'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[8])').extract()
        #web_item['cambioResidencia'] = response.xpath('normalize-space(//*[@id="MainContainer"]/article/section[1]/div[2]/ul/li[9])').extract()


        self.item_count += 1  # contador
        if self.item_count >6:  #limite de cuentas paginas hacemos scraping
            raise CloseSpider('item_exceeded')
        yield web_item

#para ejecutar https://dev.to/stankukucka/how-to-install-scrapy-on-mac-12dg
    