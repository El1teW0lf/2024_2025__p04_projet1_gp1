from modules.converter import check_if_valid_input, converter
from modules.logger import LOG
from modules.data import DATA

data = DATA()

# Define common base constants
BINARY = data.test["BIN"]
DECIMAL = data.test["DEC"]
HEXADECIMAL = data.test["HEX"]


def assert_valid_input(number, source_base, target_base, expected_result, error_counter):
    """Verifies the validity of input by checking if the number is valid for the given bases."""
    description = (
        f"Checking input: {number} from {source_base.upper()} to {target_base.upper()}"
    )
    try:
        result = check_if_valid_input(number, source_base, target_base)
        assert result == expected_result, f"Failed: {description}, got: {result}, expected: {expected_result}"
        LOG(f"{description}: ✅", 1)
    except AssertionError as e:
        LOG(f"{description}: ❌ - {e}", 1)
        error_counter[0] += 1  # Increment the error counter


def assert_conversion(number, source_base, target_base, expected_result, error_counter):
    """Verifies that the conversion result is as expected."""
    description = (
        f"Converting {number} from {source_base.upper()} to {target_base.upper()}"
    )
    try:
        result = converter(number, source_base, target_base)
        assert str(result) == str(expected_result), f"Failed: {description}, got: {result}, expected: {expected_result}"
        LOG(f"{description}: ✅", 1)
    except AssertionError as e:
        LOG(f"{description}: ❌ - {e}", 1)
        error_counter[0] += 1  # Increment the error counter


def test_check_if_valid_input():
    """Test cases to validate the input for different base conversions."""
    error_counter = [0]  # Use a list to allow mutation

    # Binary base tests
    assert_valid_input("1010", BINARY, HEXADECIMAL, True, error_counter)  # valid binary to hex
    assert_valid_input("1012", BINARY, DECIMAL, False, error_counter)  # invalid binary number
    assert_valid_input("1001", BINARY, BINARY, True, error_counter)  # valid binary to binary
    assert_valid_input("110", BINARY, DECIMAL, True, error_counter)  # valid binary to decimal

    # Decimal base tests
    assert_valid_input("123", DECIMAL, HEXADECIMAL, True, error_counter)  # valid decimal to hex
    assert_valid_input("-123", DECIMAL, BINARY, False, error_counter)  # negative numbers not allowed
    assert_valid_input("456", DECIMAL, DECIMAL, True, error_counter)  # valid decimal to decimal
    assert_valid_input("12.5", DECIMAL, HEXADECIMAL, False, error_counter)  # invalid floating-point

    # Hexadecimal base tests
    assert_valid_input("A1B", HEXADECIMAL, BINARY, True, error_counter)  # valid hex to binary
    assert_valid_input("G1", HEXADECIMAL, DECIMAL, False, error_counter)  # 'G' is not a valid hex digit
    assert_valid_input("1F4", HEXADECIMAL, HEXADECIMAL, True, error_counter)  # valid hex to hex
    assert_valid_input("2AF", HEXADECIMAL, DECIMAL, True, error_counter)  # valid hex to decimal

    # Edge cases
    assert_valid_input("0", BINARY, DECIMAL, True, error_counter)  # valid: 0 is a valid binary number
    assert_valid_input("0", DECIMAL, HEXADECIMAL, True, error_counter)  # valid: 0 is a valid decimal number
    assert_valid_input("0", HEXADECIMAL, BINARY, True, error_counter)  # valid: 0 is a valid hex number

    # Invalid base tests
    assert_valid_input("123", "xyz", HEXADECIMAL, False, error_counter)  # invalid source base
    assert_valid_input("123", DECIMAL, "abc", False, error_counter)  # invalid target base

    if error_counter[0] == 0:
        LOG("All input validation tests passed!", 1)
    else:
        LOG(f"Input validation tests finished with {error_counter[0]} errors.", 1)


def test_converter():
    """Test cases to verify base conversions."""
    error_counter = [0]  # Use a list to allow mutation

    # Binary to other bases
    assert_conversion("1010", BINARY, HEXADECIMAL, "a", error_counter)
    assert_conversion("1010", BINARY, DECIMAL, "10", error_counter)

    # Hexadecimal to other bases
    assert_conversion("a", HEXADECIMAL, BINARY, "1010", error_counter)
    assert_conversion("a", HEXADECIMAL, DECIMAL, "10", error_counter)

    # Decimal to other bases
    assert_conversion("10", DECIMAL, BINARY, "1010", error_counter)
    assert_conversion("10", DECIMAL, HEXADECIMAL, "a", error_counter)

    # Edge case: conversions of zero
    assert_conversion("0", DECIMAL, BINARY, "0", error_counter)
    assert_conversion("0", DECIMAL, HEXADECIMAL, "0", error_counter)
    assert_conversion("0", BINARY, DECIMAL, "0", error_counter)
    assert_conversion("0", HEXADECIMAL, DECIMAL, "0", error_counter)

    if error_counter[0] == 0:
        LOG("All conversion tests passed!", 1)
    else:
        LOG(f"Conversion tests finished with {error_counter[0]} errors.", 1)


def run_tests():
    test_converter()
    test_check_if_valid_input()