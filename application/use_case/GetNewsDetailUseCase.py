class GetNewsDetailUseCase:
    def __init__(self, news_repository_dataset):
        self._newsRepositoryDataset = news_repository_dataset

    def execute(self, news_id):
        news_id = int(news_id)
        df = self._newsRepositoryDataset.get_news()
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
