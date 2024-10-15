class DATA:
    def __init__(self):
        self.errors = {
            "INVALID_START_BASE": "Veuillez entrer une base de départ valide",
            "INVALID_TARGET_BASE": "Veuillez entrer une base cible valide",
            "NOT_HEX_NUMBER": "Ce n'est pas un nombre hexadécimal",
            "NOT_DECIMAL_NUMBER": "Ce n'est pas un nombre décimal",
            "NOT_BINARY_NUMBER": "Ce n'est pas un nombre binaire",
            "NON_NUMERIC_CHARACTER": "Cela contient des caractères non numériques",
            "INVALID_SIGN": "Le nombre doit être >= 0",
            "MISSING_PACKAGES": "Vous avez besoin du paquet 'keyboard' pour exécuter ce projet. Veuillez exécuter 'pip install .'"
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
           "INT_CHAR_MAP": {'&': '1', 'é': '2', '"': '3',"1":"1","2":"2","3":"3"},
            "COMPLETE_CHAT_MAP": {'&': '1', 'é': '2', '"': '3', "'": '4','(': '5', '§': '6','-': '-', 'è': '7', '!': '8','_': '8','ç': '9', 'à': '0',"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0","a":"a","b":"b","c":"c","d":"d","e":"e","f":"f"}
        }

        self.test = {
            "BIN":"bin",
            "DEC":"dec",
            "HEX":"hex"
        }
    def get_error(self, error_key):
        return self.errors.get(error_key, "Unknown error")
