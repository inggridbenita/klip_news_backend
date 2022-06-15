import pandas as pd
from domains.News.NewsRepository import NewsRepository


class NewsRepositoryDataset(NewsRepository):
    def get_news_preprocessed(self):
        return pd.read_csv("./res/datasets/news_preprocessed.csv")

    def get_news(self):
        return pd.read_csv("./res/datasets/news.csv")
