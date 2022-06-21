from commons.InvariantError import InvariantError


class DomainErrorTranslator:
    def __init__(self):
        self.directories = {
            'GET_NEWS_DETAIL_USE_CASE.NOT_CONTAIN_NEEDED_PROPERTY': InvariantError('News id must be sent'),
            'GET_NEWS_DETAIL_USE_CASE.NOT_MEET_DATA_TYPE_SPECIFICATION': InvariantError('News id must be string'),
        }

    def translate(self, error_message):
        if error_message in self.directories:
            return self.directories[error_message]
        else:
            raise Exception('error_message not found')
