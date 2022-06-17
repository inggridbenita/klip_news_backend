class GetRecommendationUseCase:
    def __init__(self, news_repository_dataset, rake_repository_library, basic_operation):
        self._newsRepositoryDataset = news_repository_dataset
        self._rakeRepositoryLibrary = rake_repository_library
        self._basicOperation = basic_operation

    def execute(self, news_id_arr):
        df_news_preprocessed = self._newsRepositoryDataset.get_news_preprocessed()  # Get news preprocessed dataset
        df_stopwords = self._newsRepositoryDataset.get_stopwords()  # Get news preprocessed dataset

        # Get recommendation with rake algorithm
        recommended_news = self._rakeRepositoryLibrary\
            .get_recommendation(df_news_preprocessed, df_stopwords, news_id_arr)

        # wrap news array with mapping format
        # this action is required because with mapping format, array can be serialized
        return self._basicOperation.wrap_value_with_mapping_format(recommended_news, "news")
