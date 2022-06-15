from domains.DataFrame.DataFrameRepository import DataFrameRepository


class DataFrameRepositoryLibrary(DataFrameRepository):
    def filter_by_single_column_with_single_value(self, df, column_name, value):
        return df[df[column_name] == value]

    def filter_by_single_column_with_multiple_value(self, df, column_name, array):
        return df[df[column_name].isin(array)]

    def get_single_column(self, df, index):
        return df.iloc[index]

    def get_array_of_column_names(self, df):
        return df.columns.values.tolist()
