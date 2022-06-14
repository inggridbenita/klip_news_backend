from application.use_case.GetAllNewsUseCase import GetAllNewsUseCase
from application.use_case.GetNewsDetailUseCase import GetNewsDetailUseCase
from infrastructure.Repository.NewsRepositoryDataset import NewsRepositoryDataset
from infrastructure.Repository.DateTimeRepositoryLibrary import DateTimeRepositoryLibrary


def get_all_news_handler():
    news_repository_dataset = NewsRepositoryDataset()
    datetime_repository = DateTimeRepositoryLibrary()
    use_case = GetAllNewsUseCase(news_repository_dataset, datetime_repository)
    news = use_case.execute()
    return news


def get_news_detail_handler(news_id):
    news_repository_dataset = NewsRepositoryDataset()
    use_case = GetNewsDetailUseCase(news_repository_dataset)
    news = use_case.execute(news_id)
    return news
