from logger import LOG
from data import DATA

data = DATA()


def converter(init_number, init_base, target_base):
    bases = ["bin", "dec", "hex"]
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    if not init_base in bases:
        LOG(data.get_error("INVALID_START_BASE"), 3)
        return 0

    if not target_base in bases:
        LOG(data.get_error("INVALID_TARGET_BASE"), 3)
        return 0

    for c in str(init_number):
        if init_base == "hex" and not c in hex_map:
            LOG(data.get_error("NOT_HEX_NUMBER"), 3)
            return 0
        elif not is_number(c):
            if init_base == "dec":
                LOG(data.get_error("NOT_DECIMAL_NUMBER"), 3)
                return 0
            elif init_base == "bin":
                LOG(data.get_error("NOT_BINARY_NUMBER"), 3)
                return 0
        elif init_base == "bin" and int(c) > 1:
            LOG(data.get_error("NOT_BINARY_NUMBER"), 3)
            return 0

        
    # Errors handled, we can start the convertion
    if init_base == target_base:
        return init_number

    
    if init_base == "bin":
        init_number = bin_to_dec(init_number)
    elif init_base == "hex":
        init_number = hex_to_dec(init_number)
    

    if target_base == "bin":
        return dec_to_bin(init_number)
    elif target_base == "hex":
        return dec_to_hex(init_number)

    
    return str(init_number)

def is_number(c):
    is_int = False
    try:
        value = int(c)
        is_int = True
    except:
        pass
    return is_int

def hex_to_dec(init_number):
    target_number = ""
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    v1 = []
    for i in init_number:
        for b in hex_map:
            if i == b:
                v1.append(hex_map.index(b))

    target_number = 0
    a = len(v1) - 1
    
    for n in v1:
        n = int(n)
        target_number += n * 16**a
        a-=1
    
    return target_number

def dec_to_hex(init_number):
    target_number = ""
    n = int(init_number)
    hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    while n > 0:
        a = n % 16
        target_number += str(hex_map[a])
        n //= 16

    target_number = target_number[::-1]
    return target_number

def dec_to_bin(init_number):

    target_number = ""
    n = int(init_number)
    while n > 0:
        target_number += str(n % 2)
        n //= 2

    target_number = target_number[::-1]
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