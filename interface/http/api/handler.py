from application.use_case.GetAllNewsUseCase import GetAllNewsUseCase
from application.use_case.GetNewsDetailUseCase import GetNewsDetailUseCase
from application.use_case.GetArrNewsDetail import GetArrNewsDetailUseCase
from application.use_case.GetNewsByCategoryUseCase import GetNewsByCategoryUseCase
from application.use_case.GetRecommendationUseCase import GetRecommendationUseCase
from commons.DomainErrorTranslator import DomainErrorTranslator
from infrastructure.Repository.BasicOperationRepositoryPython import BasicOperationRepositoryPython
from infrastructure.Repository.Dataset.NewsRepositoryDataset import NewsRepositoryDataset
from infrastructure.Repository.Library.DataFrameRepositoryLibrary import DataFrameRepositoryLibrary
from infrastructure.Repository.Library.RakeRepositoryLibrary import RakeRepositoryLibrary


def get_all_news_handler():
    try:
        news_repository_dataset = NewsRepositoryDataset()
        data_frame_repository_library = DataFrameRepositoryLibrary()
        basic_operation = BasicOperationRepositoryPython()
        use_case = GetAllNewsUseCase(
            news_repository_dataset,
            data_frame_repository_library,
            basic_operation
        )
        news = use_case.execute()
        return news
    except Exception as ex:
        det = DomainErrorTranslator()
        return str(det.translate(str(ex)))


def get_news_detail_handler(news_id):
    try:
        news_repository_dataset = NewsRepositoryDataset()
        data_frame_repository_library = DataFrameRepositoryLibrary()
        basic_operation = BasicOperationRepositoryPython()
        use_case = GetNewsDetailUseCase(news_repository_dataset, data_frame_repository_library, basic_operation)
        return use_case.execute(news_id)
    except Exception as ex:
        det = DomainErrorTranslator()
        return str(det.translate(str(ex)))


def get_arr_news_detail_handler(news):  # news is list of integer
    try:
        news_repository_dataset = NewsRepositoryDataset()
        data_frame_repository_library = DataFrameRepositoryLibrary()
        basic_operation = BasicOperationRepositoryPython()
        use_case = GetArrNewsDetailUseCase(news_repository_dataset, data_frame_repository_library, basic_operation)
        news = use_case.execute(news)
        return news
    except Exception as ex:
        det = DomainErrorTranslator()
        return str(det.translate(str(ex)))


def get_news_by_category_handler(category):
    try:
        news_repository_dataset = NewsRepositoryDataset()
        data_frame_repository_library = DataFrameRepositoryLibrary()
        basic_operation = BasicOperationRepositoryPython()
        use_case = GetNewsByCategoryUseCase(news_repository_dataset, data_frame_repository_library, basic_operation)
        news = use_case.execute(category)
        return news
    except Exception as ex:
        det = DomainErrorTranslator()
        return str(det.translate(str(ex)))


def get_recommendation_handler(news_id_arr):
    try:
        news_repository_dataset = NewsRepositoryDataset()
        rake_repository_library = RakeRepositoryLibrary()
        basic_operation = BasicOperationRepositoryPython()
        use_case = GetRecommendationUseCase(news_repository_dataset, rake_repository_library, basic_operation)
        news = use_case.execute(news_id_arr)
        return news
    except Exception as ex:
        det = DomainErrorTranslator()
        return str(det.translate(str(ex)))
