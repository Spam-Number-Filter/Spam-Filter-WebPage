class PostTitleValidationData:
    def __init__(self, is_valid: bool, error_message: str = None):
        self.is_valid = is_valid
        self.error_message = error_message


def valid_post_title(message: str) -> PostTitleValidationData:
    if message == "":
        return PostTitleValidationData(False, "Post title cannot be empty")
    return PostTitleValidationData(True)
