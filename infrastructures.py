import pandas as pd
import datetime
from domains import News


class NewsRepository(News):
    def get_all_news(self):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        df = pd.read_csv("./res/datasets/news_preprocessed.csv")
        list_news = []
        for i in range(0, len(df)):
            list_news.append({
                "id": str(df['id'][i]),
                "title": df['title'][i],
                "date": df['date'][i],
                "weekday": df["weekday"][i],
                "poster": df['poster'][i],
                "category": df['category'][i],
            })
        list_news = sorted(list_news, key=lambda news: datetime.datetime.strptime(news["date"], datetime_format))
        list_news.reverse()
        for i in range(0, len(df)):
            list_news[i]["date"] = datetime.datetime\
                .strptime(list_news[i]["date"], datetime_format).strftime(datetime_format)
        return list_news

    def get_news_detail(self, news_id):
        news_id = int(news_id)
        df = pd.read_csv("./res/datasets/news.csv")
        df = df[df["id"] == news_id]
        news = df.iloc[0]
        news_dict = {
            "id": str(news['id']),
            "title": news['title'],
            "date": news['date'],
            "weekday": news["weekday"],
            "poster": news['poster'],
            "category": news['category'],
            "content": news['content'],
        }
        return news_dict
