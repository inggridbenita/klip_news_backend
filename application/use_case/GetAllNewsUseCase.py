class GetAllNewsUseCase:
    def __init__(
            self,
            news_repository_dataset,
            data_frame_repository_library,
            basic_operation
    ):
        self._newsRepositoryDataset = news_repository_dataset
        self._DataFrameRepositoryLibrary = data_frame_repository_library
        self._basicOperation = basic_operation

    def execute(self):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        news_preprocessed = self._newsRepositoryDataset.get_news()  # get news preprocessed dataframe

        # Get dataframe column name
        column_names = self._DataFrameRepositoryLibrary.get_array_of_column_names(news_preprocessed)

        arr_news = []  # array for store each news
        for i in range(0, len(news_preprocessed)):
            # get single news based on iteration index
            news_item = self._DataFrameRepositoryLibrary.get_single_column(news_preprocessed, i)

            # convert news_id to from integer to string (if id in integer, data can't be serialized)
            news_item["id"] = self._basicOperation.convert_integer_to_string(news_item["id"])

            # convert single news to mapping format (in python called as dictionary)
            news_dict = self._basicOperation.convert_data_frame_row_to_mapping_format(news_item, column_names)

            # Add news to array of news
            arr_news.append(news_dict)

        # sort arr_news based on date (ascending)
        arr_news = self._basicOperation.sort_array_of_map_by_date_type_property(arr_news, 'date', datetime_format, True)

        # wrap news array with mapping format
        # this action is required because with mapping format, array can be serialized
        return self._basicOperation.wrap_value_with_mapping_format(arr_news, "news")
