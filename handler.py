import application
from infrastructures import NewsRepository


def get_all_news_handler():
    news_repository = NewsRepository()
    use_case = application.GetAllNewsUseCase(news_repository)
    news = use_case.execute()
    return news


def get_news_detail_handler(news_id):
    news_repository = NewsRepository()
    use_case = application.GetNewsDetailUseCase(news_repository)
    news = use_case.execute(news_id)
    return news
