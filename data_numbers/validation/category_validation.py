VALID_CATEGORIES = ["Spam", "Scam", "Advertise"]


class CategoryValidationData:
    def __init__(self, is_valid: bool, error_message: str = None):
        self.is_valid = is_valid
        self.error_message = error_message


def valid_category(category: str) -> CategoryValidationData:
    if category not in VALID_CATEGORIES:
        return CategoryValidationData(False, "A category must be chosen")
    return CategoryValidationData(True)
