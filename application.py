class GetAllNewsUseCase:
    def __init__(self, news_repository):
        self._newsRepository = news_repository

    def execute(self):
        news = self._newsRepository.get_all_news()
        return {"news": news}


class GetNewsDetailUseCase:
    def __init__(self, news_repository):
        self._newsRepository = news_repository

    def execute(self, news_id):
        news = self._newsRepository.get_news_detail(news_id)
        return news
