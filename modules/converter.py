# Main convertions functions : @GoldyRat
# Error handler : @GoldyRat et @Herasium

from modules.logger import LOG
from modules.data import DATA

data = DATA()

hex_map = data.convert["HEXA_MAP"]
bases = data.convert["BASES"]


def is_natural(c):
    is_int = False
    try:  # if the convertion of the character to an integer isn't working, then it's not a number
        value = int(c)
        is_int = True
        if int(c) >= 0:   # if the number is negative, it's not a natural number

            is_int  = True 

    except:
        pass

    return is_int


def hex_to_dec(init_number):
    v1 = []
    for i in init_number:
        for b in hex_map:
            if i == b:
                v1.append(
                    hex_map.index(b)
                )  # converting the hexadecimal number to a list with all of the coefficients

    target_number = 0
    a = len(v1) - 1

    for n in v1:
        n = int(n)
        target_number += n * 16**a
          # Writing the hexadecimal number as a sum of numbers multiplied by the highest possible power of 16
        a -= 1  # Reducing the power as we continue the loop

    return target_number


def dec_to_hex(init_number):
    target_number = ""
    n = int(init_number)

    while n > 0:
        a = n % 16
        target_number += str(hex_map[a])
        n //= 16

    target_number = target_number[::-1]  # Reversing the loop to get the final number
    return target_number


def dec_to_bin(init_number):
    target_number = ""
    n = int(init_number)
    while n > 0:  # When the result of the euclidian division of the number by 2 reaches 0, we stop the loop
        target_number += str(n % 2)  # Adding the coefficient to the final number
        n //= 2  # Dividing the number by 2 while keeping it int as we continue the loop

    target_number = target_number[::-1]  # Reversing the loop to get the final number
    return target_number


def bin_to_dec(init_number):
    target_number = 0
    a = len(init_number) - 1

    for n in init_number:
        n = int(n)
        target_number += n * 2**a
        a -= 1

    return str(target_number)


def check_if_valid_input(number, base, target):
    """
    Vérifie si l'entrée (nombre, base initiale, base cible) est valide.
    Gère les erreurs liées aux bases invalides, aux signes incorrects, et aux caractères non valides.

    J'ai ecrit le code inital, refactorisé mieux par chatgpt, j'avoue que le resultat final est cool. //Victor
    """
    number = str(number).lower()

    # Vérification de la validité des bases source et cible
    if base not in bases:
        LOG(data.get_error("INVALID_START_BASE"), 3)
        return False, "INVALID_START_BASE"

    if target not in bases:
        LOG(data.get_error("INVALID_TARGET_BASE"), 3)
        return False, "INVALID_TARGET_BASE"

    # Dictionnaire pour associer chaque base à son validateur de caractères
    base_validators = {
        "hex": lambda c: c in hex_map,
        "dec": lambda c: c.isdigit(),
        "bin": lambda c: c in "01",
    }

    # Validation des caractères du nombre en fonction de la base
    validator = base_validators.get(base)

    if not validator:
        LOG(data.get_error("INVALID_START_BASE"), 3)
        return False, "INVALID_START_BASE"

    # Vérification caractère par caractère
    for c in str(number):
        if not validator(c):
            error_key = {
                "hex": "NOT_HEX_NUMBER",
                "dec": "NOT_DECIMAL_NUMBER",
                "bin": "NOT_BINARY_NUMBER",
            }[base]
            LOG(data.get_error(error_key), 3)
            return False, error_key

    # Vérification des nombres décimaux négatifs
    if base == "dec" and int(number) < 0:
        LOG(data.get_error("INVALID_SIGN"), 3)
        return False, "INVALID_SIGN"

    return True,""

#J'ai fait la fonction mais elle était moche du coup j'ai demandé à Chat GPT de remixer un coup
def converter(init_number, init_base, target_base):
    init_number = str(init_number).lower()
    valid, mess = check_if_valid_input(init_number, init_base, target_base)
   
    try:
        if not valid:
            return False, mess
    except:
        LOG(data.get_error("Unknown", 3))
        return False,mess

    # Errors handled, we can start the convertion
    if init_base == target_base:
        return init_number,None

    if init_number == "0":
        return init_number,None #0 c'est toujours 0 peu importe la base + 0 faisait crash le code en input donc j'ai rajouté cette ligne 

    # Converting the number to decimal if not already done
    if init_base == "bin":
        init_number = bin_to_dec(init_number)
    elif init_base == "hex":
        init_number = hex_to_dec(init_number)

    # If needed, converting the decimal to binary or hexadecimal
    if target_base == "bin":
        return dec_to_bin(init_number),None
    elif target_base == "hex":
        return dec_to_hex(init_number),None

    return str(init_number),None
