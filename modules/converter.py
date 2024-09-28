# Main convertions functions : @GoldyRat
# Error handler : @GoldyRat et @Herasium

from logger import LOG
from data import DATA

data = DATA()


def converter(init_number, init_base, target_base):
    bases = ["bin", "dec", "hex"]
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]# Every hexadecimal characters

    if not init_base in bases: # check if the init base is a base
        LOG(data.get_error("INVALID_START_BASE"), 3)
        return 0

    if not target_base in bases: # same for the target base
        LOG(data.get_error("INVALID_TARGET_BASE"), 3)
        return 0

    for c in str(init_number):
        if init_base == "hex" and not c in hex_map:  # if every character of the string is a base 16 number and the init base is hex, we can continue
            LOG(data.get_error("NOT_HEX_NUMBER"), 3)
            return 0
        elif not is_number(c): # checking if every character of the string is a number, else the program won't work
            if init_base == "dec":
                LOG(data.get_error("NOT_DECIMAL_NUMBER"), 3)
                return 0
            elif init_base == "bin":
                LOG(data.get_error("NOT_BINARY_NUMBER"), 3)
                return 0
        elif init_base == "bin" and int(c) > 1: # verifying that the number only has 0 or 1, else it's not binary
                LOG(data.get_error("NOT_BINARY_NUMBER"), 3)
                return 0
        elif init_base == "bin" and int(c) > 1:
            LOG(data.get_error("NOT_BINARY_NUMBER"), 3)
            return 0

        
    # Errors handled, we can start the convertion
    if init_base == target_base:
        return init_number

    # Converting the number to decimal if not already done
    if init_base == "bin":
        init_number = bin_to_dec(init_number)
    elif init_base == "hex":
        init_number = hex_to_dec(init_number)
    
    # If needed, converting the decimal to binary or hexadecimal
    if target_base == "bin":
        return dec_to_bin(init_number)
    elif target_base == "hex":
        return dec_to_hex(init_number)

    
    return str(init_number)

def is_number(c):
    is_int = False
    try: # if the convertion of the character to an integer isn't working, then it's not a number
        value = int(c)
        is_int = True
    except:
        pass
    return is_int

def hex_to_dec(init_number):
    
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"] # Every hexadecimal characters
    v1 = []
    for i in init_number:
        for b in hex_map: 
            if i == b:
                v1.append(hex_map.index(b)) # converting the hexadecimal number to a list with all of the coefficients

    target_number = 0
    a = len(v1) - 1
    
    for n in v1:
        n = int(n)
        target_number += n * 16**a # Writing the hexadecimal number as a sum of numbers multiplied by the highest possible power of 16
        a-=1 # Reducing the power as we continue the loop
    
    return target_number

def dec_to_hex(init_number):
    target_number = ""
    n = int(init_number)
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"] # Every hexadecimal characters
    while n > 0: # When the result of the euclidian division of the number by 16 reaches 0, we stop the loop
        a = n % 16 # The coefficient a is equal to n modulo 16
        target_number += str(hex_map[a]) # Converting the coefficient a to it's equivalent in hexadecimal and adding it to the target number chain
        n //= 16 # Dividing the number by 16 while keeping it int as we continue the loop

    target_number = target_number[::-1] # Reversing the loop to get the final number
    return target_number

def dec_to_bin(init_number):

    target_number = ""
    n = int(init_number)
    while n > 0: # When the result of the euclidian division of the number by 2 reaches 0, we stop the loop
        target_number += str(n % 2) # Adding the coefficient to the final number
        n //= 2 # Dividing the number by 2 while keeping it int as we continue the loop

    target_number = target_number[::-1] # Reversing the loop to get the final number
    return target_number

def bin_to_dec(init_number):

    target_number = 0
    a = len(init_number) - 1
    
    for n in init_number:
        n = int(n)
        target_number += n * 2**a
        a-=1 
    
    return target_number



print(converter("a10","dec","hex"))