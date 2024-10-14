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
            "MISSING_PACKAGES": "You need the keyboard package to run this project. Please run 'pip install .'"
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

        self.log = {
            "PREFIX": ["DEBUG", "TEST", "INFO", "\033[31;1m☢️ERROR☢️\033[0m"]
        }
        
        self.ui = {
            "LOGO": """    ____  __________  _   ___    ____________  ______
   / __ )/ ____/ __ \/ | / / |  / / ____/ __ \/_  __/
  / __  / /   / / / /  |/ /| | / / __/ / /_/ / / /   
 / /_/ / /___/ /_/ / /|  / | |/ / /___/ _, _/ / /    
/_____/\____/\____/_/ |_/  |___/_____/_/ |_| /_/     """,
            "COLOR_1": "ff99c8",
            "COLOR_2": "e4c1f9",
            "COLORS": ["ffadad","ffd6a5","fdffb6","caffbf","9bf6ff","a0c4ff","bdb2ff","ffc6ff","fffffc"],
            "RANDOM_COLORS": True,
            "COLORED": True,
            "GRAD_STEP": 70,
            "CHAR_MAP": {
    '&': '1', 'é': '2', '"': '3', "'": '4',
    '(': '5', '§': '6', 'è': '7', '!': '8',
    'ç': '9', 'à': '0',"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0"
}
        }


        self.test = {
            "BIN":"bin",
            "DEC":"dec",
            "HEX":"hex"
        }
    def get_error(self, error_key):
        return self.errors.get(error_key, "Unknown error")
