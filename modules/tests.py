from converter import check_if_valid_input, converter

# Define common base constants
BINARY = "bin"
DECIMAL = "dec"
HEXADECIMAL = "hex"

def assert_valid_input(number, source_base, target_base, expected_result):
    """Verifies the validity of input by checking if the number is valid for the given bases."""
    result = check_if_valid_input(number, source_base, target_base)
    description = f"Checking input: {number} from {source_base.upper()} to {target_base.upper()}"
    assert result == expected_result, f"Failed: {description}, got: {result}, expected: {expected_result}"


def assert_conversion(number, source_base, target_base, expected_result):
    """Verifies that the conversion result is as expected."""
    result = converter(number, source_base, target_base)
    description = f"Converting {number} from {source_base.upper()} to {target_base.upper()}"
    assert str(result) == str(expected_result), f"Failed: {description}, got: {result}, expected: {expected_result}"




def test_check_if_valid_input():
    """Test cases to validate the input for different base conversions."""
    
    # Binary base tests
    assert_valid_input("1010", BINARY, HEXADECIMAL, True)   # valid binary to hex
    assert_valid_input("1012", BINARY, DECIMAL, False)      # invalid binary number (2 is not a valid binary digit)
    assert_valid_input("1001", BINARY, BINARY, True)        # valid binary to binary
    assert_valid_input("110", BINARY, DECIMAL, True)        # valid binary to decimal

    # Decimal base tests
    assert_valid_input("123", DECIMAL, HEXADECIMAL, True)   # valid decimal to hex
    assert_valid_input("-123", DECIMAL, BINARY, False)      # negative numbers not allowed
    assert_valid_input("456", DECIMAL, DECIMAL, True)       # valid decimal to decimal
    assert_valid_input("12.5", DECIMAL, HEXADECIMAL, False) # invalid floating-point decimal number

    # Hexadecimal base tests
    assert_valid_input("A1B", HEXADECIMAL, BINARY, True)    # valid hex to binary
    assert_valid_input("G1", HEXADECIMAL, DECIMAL, False)   # 'G' is not a valid hex digit
    assert_valid_input("1F4", HEXADECIMAL, HEXADECIMAL, True) # valid hex to hex
    assert_valid_input("2AF", HEXADECIMAL, DECIMAL, True)   # valid hex to decimal

    # Edge cases
    assert_valid_input("0", BINARY, DECIMAL, True)          # valid: 0 is a valid binary number
    assert_valid_input("0", DECIMAL, HEXADECIMAL, True)     # valid: 0 is a valid decimal number
    assert_valid_input("0", HEXADECIMAL, BINARY, True)      # valid: 0 is a valid hex number

    # Invalid base tests
    assert_valid_input("123", "xyz", HEXADECIMAL, False)    # invalid source base
    assert_valid_input("123", DECIMAL, "abc", False)        # invalid target base

    print("All input validation tests passed!")


def test_converter():
    """Test cases to verify base conversions."""
    
    # Binary to other bases
    assert_conversion("1010", BINARY, HEXADECIMAL, "a")
    assert_conversion("1010", BINARY, DECIMAL, "10")

    # Hexadecimal to other bases
    assert_conversion("a", HEXADECIMAL, BINARY, "1010")
    assert_conversion("a", HEXADECIMAL, DECIMAL, "10")

    # Decimal to other bases
    assert_conversion("10", DECIMAL, BINARY, "1010")
    assert_conversion("10", DECIMAL, HEXADECIMAL, "a")

    # Edge case: conversions of zero
    assert_conversion("0", DECIMAL, BINARY, "0")
    assert_conversion("0", DECIMAL, HEXADECIMAL, "0")
    assert_conversion("0", BINARY, DECIMAL, "0")
    assert_conversion("0", HEXADECIMAL, DECIMAL, "0")

    print("All conversion tests passed!")
