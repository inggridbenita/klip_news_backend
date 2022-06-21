class ClientError(Exception):
    def __init__(self, status_code=400):
        super()

        self.status_code = status_code
        self.name = 'Client Error'
        if self.__class__.__name__ == 'ClientError':
            raise Exception('Cannot instance abstract class')
