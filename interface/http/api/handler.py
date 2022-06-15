from application.use_case.GetAllNewsUseCase import GetAllNewsUseCase
from application.use_case.GetNewsDetailUseCase import GetNewsDetailUseCase
from application.use_case.GetArrNewsDetail import GetArrNewsDetailUseCase
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


def get_arr_news_detail_handler(news):  # news is list of integer
    news_repository_dataset = NewsRepositoryDataset()
    use_case = GetArrNewsDetailUseCase(news_repository_dataset)
    news = use_case.execute(news)
    return news
