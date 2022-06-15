class GetArrNewsDetailUseCase:
    def __init__(self, news_repository_dataset):
        self._newsRepositoryDataset = news_repository_dataset

    def execute(self, news):  # news is list of integer
        df = self._newsRepositoryDataset.get_news()
        df = df[df["id"].isin(news)]
        news = []
        for i in range(0, len(df)):
            news_item = df.iloc[i]
            news_dict = {
                "id": str(news_item['id']),
                "title": news_item['title'],
                "date": news_item['date'],
                "weekday": news_item["weekday"],
                "poster": news_item['poster'],
                "category": news_item['category'],
                "content": news_item['content'],
            }
            news.append(news_dict)
        return {"news": news}
