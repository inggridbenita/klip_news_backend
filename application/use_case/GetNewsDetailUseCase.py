class GetNewsDetailUseCase:
    def __init__(self, news_repository_dataset, data_frame_repository_library, basic_operation):
        self._newsRepositoryDataset = news_repository_dataset
        self._dataFrameRepositoryLibrary = data_frame_repository_library
        self._basicOperation = basic_operation

    def execute(self, news_id):
        self._validate_id(news_id)
        news_id = self._basicOperation.convert_string_to_integer(news_id)  # Convert news id to integer
        df = self._newsRepositoryDataset.get_news()  # get news dataset
        column_names = self._dataFrameRepositoryLibrary.get_array_of_column_names(df)  # get dataframe column names

        # Filter dataframe based on news id
        df = self._dataFrameRepositoryLibrary.filter_by_single_column_with_single_value(df, 'id', news_id)

        news_item = self._dataFrameRepositoryLibrary.get_single_column(df, 0)  # get first column

        # convert news_id to from integer to string (if id in integer, data can't be serialized)
        news_item["id"] = self._basicOperation.convert_integer_to_string(news_item["id"])

        # convert single news to mapping format (in python called as dictionary)
        news_dict = self._basicOperation.convert_data_frame_row_to_mapping_format(news_item, column_names)

        return news_dict

    @staticmethod
    def _validate_id(id):
        if isinstance(id, type(None)):
            raise Exception('GET_NEWS_DETAIL_USE_CASE.NOT_CONTAIN_NEEDED_PROPERTY')

        if not isinstance(id, str):
            raise Exception('GET_NEWS_DETAIL_USE_CASE.NOT_MEET_DATA_TYPE_SPECIFICATION')
