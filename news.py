from gnews import GNews


class Noticia:
    def __init__(self):
        google_news = GNews()
        google_news.language = 'pt-br'
        google_news.max_results = 10
        google_news.country = 'Brazil'
        google_news.period = '3d'
        busca = 'mercado de ações'
        result = google_news.get_news(busca)

        for x in result:
            print("Titulo: ", x['title'])
            print("Data ", x['published date'])
            print("Descrição---", x['description']),
            print("Link--- ", x['url'])
