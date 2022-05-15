import os
from abc import ABC, abstractmethod
from typing import Dict

import requests
from requests import Response


class NumberValidationData:
    def __init__(self, is_valid: bool, error_message: str = None):
        self.is_valid = is_valid
        self.error_message = error_message


class NumberValidation(ABC):
    """
    Abstract class for number validation. Necessary since, if we want to do a number validation
    test, we need to mock it.
    """

    @abstractmethod
    def valid_number(self) -> NumberValidationData:
        pass


class ApiNumberValidation(NumberValidation):
    """
    Validates a number using the https://app.abstractapi.com/api/phone-validation/ api
    Requires an API key, which the host should have as an environment variable. An example is:
    PHONE_API_KEY="YOUR_API_KEY"
    Be aware that we have to mock this API for testing purposes, since the API has a limit of 250 requests per month.
    """

    def __init__(self, prefix: int, number: int):
        self.api_string = ApiNumberValidation._get_api_string(prefix, number)

    @staticmethod
    def _get_api_string(prefix: int, number: int) -> str:
        api_key_env = os.environ.get("PHONE_API_KEY", "api key is not valid")
        return f"https://phonevalidation.abstractapi.com/v1/?{api_key_env}&phone=+{prefix}{number}"

    def valid_number(self) -> NumberValidationData:
        response: Response = requests.get(self.api_string)
        if response.status_code != 200:
            return NumberValidationData(False, "There was an error with the API call")
        return ApiNumberValidation.parse_response(response)

    @staticmethod
    def parse_response(response: Response) -> NumberValidationData:
        response_content: Dict[str] = response.json()
        if response_content["valid"] is False:
            return NumberValidationData(False, "The number is not valid")
        return NumberValidationData(True)
