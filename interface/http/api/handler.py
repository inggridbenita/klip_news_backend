from application.use_case.GetAllNewsUseCase import GetAllNewsUseCase
from application.use_case.GetNewsDetailUseCase import GetNewsDetailUseCase
from application.use_case.GetArrNewsDetail import GetArrNewsDetailUseCase
from commons.BasicOperation import BasicOperation
from infrastructure.Repository.Dataset.NewsRepositoryDataset import NewsRepositoryDataset
from infrastructure.Repository.Library.DataFrameRepositoryLibrary import DataFrameRepositoryLibrary


def get_all_news_handler():
    news_repository_dataset = NewsRepositoryDataset()
    data_frame_repository_library = DataFrameRepositoryLibrary()
    basic_operation = BasicOperation()
    use_case = GetAllNewsUseCase(
        news_repository_dataset,
        data_frame_repository_library,
        basic_operation
    )
    news = use_case.execute()
    return news


def get_news_detail_handler(news_id):
    news_repository_dataset = NewsRepositoryDataset()
    data_frame_repository_library = DataFrameRepositoryLibrary()
    basic_operation = BasicOperation()
    use_case = GetNewsDetailUseCase(news_repository_dataset, data_frame_repository_library, basic_operation)
    news = use_case.execute(news_id)
    return news


def get_arr_news_detail_handler(news):  # news is list of integer
    news_repository_dataset = NewsRepositoryDataset()
    data_frame_repository_library = DataFrameRepositoryLibrary()
    basic_operation = BasicOperation()
    use_case = GetArrNewsDetailUseCase(news_repository_dataset, data_frame_repository_library, basic_operation)
    news = use_case.execute(news)
    return news
