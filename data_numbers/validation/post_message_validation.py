class PostMessageValidationData:
    def __init__(self, is_valid: bool, error_message: str = None):
        self.is_valid = is_valid
        self.error_message = error_message


def valid_post_message(message: str) -> PostMessageValidationData:
    if not isinstance(message, str) or len(message) == 0:
        return PostMessageValidationData(False, "Post message cannot be empty")
    return PostMessageValidationData(True)
