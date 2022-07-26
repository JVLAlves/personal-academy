class NonExistentError(Exception):
    """ Raised when the operator does not exists in the Database

    attributes:

    name - The name which triggered the error
    message - The error message
    """
    def __init__(self, name:str, message:str="This operator does not exists in the Database"):
        self.name = name
        self.message = message
        super(NonExistentError, self).__init__(self.message)

    def __str__(self):
        return f"'{self.name}' ==> {self.message}"