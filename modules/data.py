class DATA:
    def __init__(self):
        self.errors = {
            "INVALID_START_BASE": "Please enter a valid init base",
            "INVALID_TARGET_BASE": "Please enter a valid target base",
            "NOT_HEX_NUMBER": "This is not a hexadecimal number",
            "NOT_DECIMAL_NUMBER": "This is not a decimal number",
            "NOT_BINARY_NUMBER": "This is not a binary number",
            "NON_NUMERIC_CHARACTER": "This contains non-numeric characters",
            "INVALID_SIGN": "The number should be >= 0",
        }

        self.convert = {
            "HEXA_MAP": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            ],
            "BASES": ["bin", "dec", "hex"],
        }

        self.ui = {
            "LOGO": """
██████╗  ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗
██╔══██╗██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   
██╔══██╗██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   
██████╔╝╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   
╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   
""",
            "COLOR_1": "ff99c8",
            "COLOR_2": "e4c1f9",
            "COLORS": ["ffadad","ffd6a5","fdffb6","caffbf","9bf6ff","a0c4ff","bdb2ff","ffc6ff","fffffc"],
            "RANDOM_COLORS": True,
            "COLORED": True,
            "GRAD_STEP": 70
        }


        self.test = {
            "BIN":"bin",
            "DEC":"dec",
            "HEX":"hex"
        }
    def get_error(self, error_key):
        return self.errors.get(error_key, "Unknown error")
