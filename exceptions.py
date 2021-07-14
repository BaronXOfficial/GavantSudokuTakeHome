class InputRowLengthException(Exception):
    """Basic Exception if Row Length of any row in input is invalid"""
    def __init__(self, msg=None):
        self.msg = msg
        if msg is None:
            self.msg = "Solution Failed - Invalid Row Length in Input"
        super(InputRowLengthException, self).__init__(msg)

class InputColumnLengthException(Exception):
    """Basic Exception if Column Length of input is invalid"""
    def __init__(self, msg=None):
        self.msg = msg
        if msg is None:
            self.msg = "Solution Failed - Invalid Column Length in Input"
        super(InputColumnLengthException, self).__init__(msg)


class SolutionFailedException(Exception):
    """Basic Exception if No Solution is Found"""
    def __init__(self, msg=None):
        self.msg = msg
        if msg is None:
            self.msg = "Solution Failed - No Solution Found"
        super(SolutionFailedException, self).__init__(msg)