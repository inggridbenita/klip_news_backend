from commons.ClientError import ClientError


class InvariantError(ClientError):
    def __init__(self, message):
        super(InvariantError, self).__init__()
        self.name = 'Invariant Error'
        self.message = message
