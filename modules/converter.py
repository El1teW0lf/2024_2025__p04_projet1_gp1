# Main convertions functions : @GoldyRat
# Error handler : @GoldyRat et @Herasium

from modules.logger import LOG
from modules.data import DATA

data = DATA()

hex_map = data.convert["HEXA_MAP"]
bases = data.convert["BASES"]

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

    return str(target_number)


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

def complement_of_2(init_number):
    if init_number[0] == "1":
        '''
            méthode du complément à 2 à  partir d'un nombre negatif (1 en premier chiffre), donc étapes inverses
        '''
        init_number = bin_to_dec(init_number)
        init_number = int(init_number) - 1 # on soustrait d'abord 1 au nombre source
        init_number = dec_to_bin(str(init_number))
        # puis on inverse chaque chiffre du nombre source
        init_number = init_number.replace("0", "2") 
        init_number = init_number.replace("1", "0")  #
        init_number = init_number.replace("2", "1")

    elif init_number[0] == "0":
        init_number = init_number.replace("0", "2") 
        init_number = init_number.replace("1", "0")  #
        init_number = init_number.replace("2", "1")
        init_number = bin_to_dec(init_number)
        init_number = int(init_number) + 1 
        init_number = dec_to_bin(str(init_number))
    return init_number

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
        "dec": lambda c: c.isdigit() or c == "-",
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
    

    return True,""

#J'ai fait la fonction mais elle était moche du coup j'ai demandé à Chat GPT de remixer un coup
def converter(init_number, init_base, target_base, from_signed = None, to_signed = None):
    is_negative = False

    init_number = str(init_number)
    for c in range(len(init_number)-1):
        if init_number[c] == "-" and c == 0:
            init_number = init_number.replace("-", "")
            is_negative = True

        elif init_number[c] == "-" and c != 0:
            LOG(data.get_error("MALFORMED_NUMBER"), 3)
            return False,data.get_error("MALFORMED_NUMBER")
    
    init_number = str(init_number).lower()
    valid, mess = check_if_valid_input(init_number, init_base, target_base)
   
    try:
        if not valid:
            return False, mess
    except:
        LOG(data.get_error("Unknown"),3)
        return False,mess
    
    init_number = str(init_number)


    # Errors handled, we can start the convertion
    if init_base == target_base:

        if init_base == target_base == "bin" and from_signed != to_signed:

            if from_signed == True:
                if init_number[0] == "0":
                    init_number = bin_to_dec(init_number)
                elif init_number[0] == "1":
                    is_negative = True
                    init_number = complement_of_2(init_number)
                    init_number = bin_to_dec(init_number)
            else:
                init_number = bin_to_dec(init_number)

            value = dec_to_bin(init_number)

            if to_signed == True:
                LOG(f"{is_negative} {value}",0)
                if not is_negative:
                    
                    value = "0" + value
                else:
                    
                    value = "0" + value
                    value =  complement_of_2(value)
                    is_negative = False
            LOG(f"{is_negative} {value}",0)

            if is_negative: value = "-" + value
            return str(value),None
        else:
            if is_negative: init_number = "-" + init_number
            return str(init_number),None

    if init_number == "0":
        if is_negative: init_number = "-" + init_number
        return str(init_number),None #0 c'est toujours 0 peu importe la base + 0 faisait crash le code en input donc j'ai rajouté cette ligne 

    # Converting the number to decimal if not already done
    if init_base == "bin":
        if from_signed == True:
            if init_number[0] == "0":
                init_number = bin_to_dec(init_number)
            elif init_number[0] == "1":
                is_negative = True
                init_number = complement_of_2(init_number)
                init_number = bin_to_dec(init_number)
        else:
            init_number = bin_to_dec(init_number)

    elif init_base == "hex":
        init_number = hex_to_dec(init_number)

    # If needed, converting the decimal to binary or hexadecimal
    if target_base == "bin":
        
        value = dec_to_bin(init_number)

        if to_signed == True:
            
            if not is_negative:
                
                value = "0" + value
            else:
                
                value = "0" + value
                value =  complement_of_2(value)
                is_negative = False
                

        if is_negative: value = "-" + value
        
        return str(value),None
    elif target_base == "hex":
        value = dec_to_hex(init_number)
        if is_negative: value = "-" + value
        return str(value),None
    
    if is_negative: init_number = "-" + init_number
    return str(init_number),None

