import os

from data_numbers.validation.number_validation import (
    ApiNumberValidation,
    NumberValidation,
    NumberValidationData,
)


def get_number_validation(prefix: int, number: int) -> NumberValidation:
    """
    Factory method to get the correct number validation class.
    If the PHONE_API_KEY is not set, it will return a simple Mock.
    @see MockingNumberValidation
    """
    if os.environ.get("PHONE_API_KEY") is None:
        return MockingNumberValidation(prefix, number)
    return ApiNumberValidation(prefix, number)


class MockingNumberValidation(NumberValidation):
    """
    Class created to mock the api calls. Only returns true if the number
    prefix length is equal to 2 and the number length is equal to 9.
    """

    def __init__(self, prefix: int, number: int):
        self.prefix = prefix
        self.number = number

    def valid_number(self) -> NumberValidationData:
        if len(str(self.prefix)) == 2 and len(str(self.number)) == 9:
            return NumberValidationData(True)
        return NumberValidationData(False, "Not an spanish number for mocks")
