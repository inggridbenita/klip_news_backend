import pandas as pd
import datetime
from domains import News
from domains import DateTime


class NewsRepository(News):
    def get_news_preprocessed(self):
        return pd.read_csv("./res/datasets/news_preprocessed.csv")

    def get_news(self):
        return pd.read_csv("./res/datasets/news.csv")


class DateTimeRepository(DateTime):
    def convert_string_to_datetime(self, datetime_string, datetime_format):
        return datetime.datetime.strptime(datetime_string, datetime_format)

    def convert_date_string_to_desired_format(self, datetime_string, datetime_format):
        return datetime.datetime.strptime(datetime_string, datetime_format).strftime(datetime_format)
