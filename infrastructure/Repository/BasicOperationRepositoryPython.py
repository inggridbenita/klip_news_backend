from domains.BasicOperationRepository import BasicOperationRepository
import datetime


class BasicOperationRepositoryPython(BasicOperationRepository):
    @staticmethod
    def convert_integer_to_string(integer):
        return str(integer)

    @staticmethod
    def convert_string_to_integer(string):
        return int(string)

    @staticmethod
    def convert_data_frame_row_to_mapping_format(df_row, column_names):
        value = {}
        for name in column_names:
            value[name] = df_row[name]
        return value

    @staticmethod
    def wrap_value_with_mapping_format(value, domain_name):
        return {domain_name: value}

    @staticmethod
    def sort_array_of_map_by_date_type_property(array, property_name, datetime_format, is_ascending):
        return sorted(array,
                      key=lambda news: datetime.datetime.strptime(news[property_name], datetime_format),
                      reverse=is_ascending)