class GetAllNewsUseCase:
    def __init__(self, news_repository, datetime_repository):
        self._newsRepository = news_repository
        self._DateTimeRepository = datetime_repository

    def execute(self):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        news_preprocessed = self._newsRepository.get_news_preprocessed()
        list_news = []
        for i in range(0, len(news_preprocessed)):
            list_news.append({
                "id": str(news_preprocessed['id'][i]),
                "title": news_preprocessed['title'][i],
                "date": news_preprocessed['date'][i],
                "weekday": news_preprocessed["weekday"][i],
                "poster": news_preprocessed['poster'][i],
                "category": news_preprocessed['category'][i],
            })
        list_news = sorted(list_news, key=lambda news: self._DateTimeRepository
                           .convert_string_to_datetime(news["date"], datetime_format))
        list_news.reverse()
        for i in range(0, len(list_news)):
            list_news[i]["date"] = self._DateTimeRepository\
                .convert_date_string_to_desired_format(list_news[i]["date"], datetime_format)
        return {"news": list_news}


class GetNewsDetailUseCase:
    def __init__(self, news_repository):
        self._newsRepository = news_repository

    def execute(self, news_id):
        news_id = int(news_id)
        df = self._newsRepository.get_news()
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
