class AlreadyExistsError(Exception):
    """Exception raised when a document already exists in the collection.
    Attributes:
        value -- the value which caused the error
        message -- explanation of the error
    """
    def __init__(self, value:dict, message:str="The document already exists."):
        self.value = value
        self.message = message
        super(AlreadyExistsError, self).__init__(self.message)

    def __str__(self):
        return f'{self.value} ==> {self.message}'

class NotExistsError(Exception):
    """Exception raised when a document NOT exists in the collection.
    Attributes:
        value -- the value which caused the error
        message -- explanation of the error
    """

    def __init__(self, value: dict, message: str = "The document not exists in the database."):
        self.value = value
        self.message = message
        super(NotExistsError, self).__init__(self.message)

    def __str__(self):
        return f'{self.value} ==> {self.message}'

