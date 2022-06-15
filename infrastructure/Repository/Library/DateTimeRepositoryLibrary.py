import datetime
from domains.DateTime.DateTimeRepository import DateTimeRepository


class DateTimeRepositoryLibrary(DateTimeRepository):
    def convert_string_to_datetime(self, datetime_string, datetime_format):
        return datetime.datetime.strptime(datetime_string, datetime_format)

    def convert_date_string_to_desired_format(self, datetime_string, datetime_format):
        return datetime.datetime.strptime(datetime_string, datetime_format).strftime(datetime_format)