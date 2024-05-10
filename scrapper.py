import json

import scrapy
from scrapy.crawler import CrawlerProcess


# scrapy crawl courses -o courses.json

class HomeSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['https://www.alura.com.br/cursos-online-tecnologia']

    def parse(self, resp):
        escolas = {} # aka category
        for escola in resp.css('.course-online-border'):
            id = escola.css('section::attr(id)').get()
            title = escola.css('.course-school-strong::text').get()
            desc = escola.css('.course-school-description::text').get()
            escolas[id] = {
                'nome': title,
                'descricao': desc,
            }

        cursos = []
        for cat in resp.css('section.lista-subcategorias'):
            escola_id = cat.css('::attr(data-category)').get()
            for sub in cat.css('.subcategoria'):
                title = sub.css('h2::text').get()
                for curso in sub.css('.card-curso'):
                    link = curso.css('::attr(href)').get()
                    nome = curso.css('.card-curso__nome::text').get()

                    data = {
                        'escola': escolas[escola_id]['nome'],
                        'categoria': title,
                        'nome': nome,
                        'link': link,
                    }
                    cursos.append(data)

        # export
        with open('escolas.json', 'w') as json_escolas:
            json.dump(escolas, json_escolas)

        with open('cursos.json', 'w') as json_cursos:
            json.dump(cursos, json_cursos)



def main():
    process = CrawlerProcess(
        settings={
            'FEEDS': {
                'items.json': {'format': 'json'},
            },
        }
    )
    process.crawl(HomeSpider)
    process.start()


if __name__ == '__main__':
    main()
