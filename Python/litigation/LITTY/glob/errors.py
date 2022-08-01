class NotHexadecimalError(Exception):
    """Exception raised when an supposed Hexadecimal value does not include the Hexadecimal indication Symbol ('#').

    Attributes:
        value -- the value which caused the error
        message -- explanation of the error
    """
    def __init__(self, value:str, message:str="missing hexadecimal symbol"):
        self.value = value
        self.message = message
        super(NotHexadecimalError, self).__init__(self.message)

    def __str__(self):
        return f'{self.value} ==> {self.message}'

class BadHexadecimalError(Exception):
    """Exception raised when an supposed Hexadecimal value is not fully alphanumeric or is missing a digit.

        Attributes:
            value -- the value which caused the error
            message -- explanation of the error
        """

    def __init__(self, value: str, message: str = "missing hexadecimal symbol"):
        self.value = value
        self.message = message
        super(BadHexadecimalError, self).__init__(self.message)

    def __str__(self):
        return f'{self.value} ==> {self.message}'

class DatabaseOutOfDateError(Exception):
    """Exception raised when it tries to search for a brand new field in the database, but it didnt found.
        Attributes:
            value -- The out of date value which caused the error
            message -- explanation of the error
    """

    def __init__(self, value: str, message: str = "is out of date. Consider recreate it or update it."):
        self.value = value
        self.message = message
        super(DatabaseOutOfDateError, self).__init__(self.message)

    def __str__(self):
        return f'{self.value} ==> {self.message}'