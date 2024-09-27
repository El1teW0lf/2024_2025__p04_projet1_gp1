
class DATA:
    def __init__(self):
        self.errors = {
            "INVALID_START_BASE": "Please enter a valid init base",
            "INVALID_TARGET_BASE": "Please enter a valid target base",
            "NOT_HEX_NUMBER": "This is not a hexadecimal number",
            "NOT_DECIMAL_NUMBER": "This is not a decimal number",
            "NOT_BINARY_NUMBER": "This is not a binary number",
            "NON_NUMERIC_CHARACTER": "This contains non-numeric characters"
        }

    def get_error(self, error_key):
        return self.errors.get(error_key, "Unknown error")
