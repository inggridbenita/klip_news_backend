import application
from infrastructures import NewsRepository
from infrastructures import DateTimeRepository


def get_all_news_handler():
    news_repository = NewsRepository()
    datetime_repository = DateTimeRepository()
    use_case = application.GetAllNewsUseCase(news_repository, datetime_repository)
    news = use_case.execute()
    return news


def get_news_detail_handler(news_id):
    news_repository = NewsRepository()
    use_case = application.GetNewsDetailUseCase(news_repository)
    news = use_case.execute(news_id)
    return news
