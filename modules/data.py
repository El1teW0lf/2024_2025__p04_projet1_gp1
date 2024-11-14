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
            "MISSING_PACKAGES": "Vous avez besoin du paquet 'keyboard' pour exécuter ce projet. Veuillez exécuter 'pip install .'",
            "MALFORMED_NUMBER": "Le nombre est malformé.",
            "INVALID_BIN_TYPE": "La reponse pour si le binaire d'entré/de sortie est signé est malformée."
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
            "COLORS": ["ff0000","ff8700","deff0a","0aff99","0aefff","147df5","580aff","be0aff"],
            "RANDOM_COLORS": True,
            "COLORED": True,
            "ANIMATED":False,
            "RAINBOW":False,
            "RAINBOW_DISTANCE":10,
            "GRAD_STEP": 70,
           "INT_CHAR_MAP": {'&': '1', 'é': '2', '"': '3',"1":"1","2":"2","3":"3"},
           "BOOL_CHAR_MAP": {'&': '1', '0': '0',"1":"1","à":"0"},
            "COMPLETE_CHAT_MAP": {'&': '1', 'é': '2', '"': '3', "'": '4','(': '5', '§': '6','-': '-', 'è': '7', '!': '8','_': '8','ç': '9', 'à': '0',"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0","a":"a","b":"b","c":"c","d":"d","e":"e","f":"f"}
        }

        self.test = {
            "BIN":"bin",
            "DEC":"dec",
            "HEX":"hex"
        }
    def get_error(self, error_key):
        return self.errors.get(error_key, "Unknown error")
