class PensionAPIException(Exception):
    def __init__(
        self,
        code: str,
        message: str,
    ):
        self.code = code
        self.message = message


class InvalidRetirementAgeException(PensionAPIException):
    def __init__(self):
        super().__init__(
            code="INVALID_RETIREMENT_AGE",
            message=("Retirement age must be greater than current age"),
        )


class InvalidTargetAmountException(PensionAPIException):
    def __init__(self):
        super().__init__(
            code="INVALID_TARGET_AMOUNT",
            message=("Target retirement amount must be greater than zero"),
        )
