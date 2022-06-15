class GetArrNewsDetailUseCase:
    def __init__(self, news_repository_dataset, data_frame_repository_library, basic_operation):
        self._newsRepositoryDataset = news_repository_dataset
        self._dataFrameRepositoryLibrary = data_frame_repository_library
        self._basicOperation = basic_operation

    def execute(self, news):  # news is list of integer
        df = self._newsRepositoryDataset.get_news()  # Get news dataset

        # filter dataframe by selected id
        df = self._dataFrameRepositoryLibrary.filter_by_single_column_with_multiple_value(df, "id", news)

        column_names = self._dataFrameRepositoryLibrary.get_array_of_column_names(df)  # get dataframe column names
        arr_news = []  # variable to store each news (array formed)
        for i in range(0, len(df)):
            # get single news based on iteration index
            news_item = self._dataFrameRepositoryLibrary.get_single_column(df, i)

            # convert news_id to from integer to string (if id in integer, data can't be serialized)
            news_item["id"] = self._basicOperation.convert_integer_to_string(news_item["id"])

            # convert single news to mapping format (in python called as dictionary)
            news_dict = self._basicOperation.convert_data_frame_row_to_mapping_format(news_item, column_names)

            # add single news to news array
            arr_news.append(news_dict)

        # wrap news array with mapping format
        # this action is required because with mapping format, array can be serialized
        return self._basicOperation.wrap_value_with_mapping_format(arr_news, "news")
