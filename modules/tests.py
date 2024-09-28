from converter import check_if_valid_input,converter

def assert_valid_input(number, base, target, expected):
    result = check_if_valid_input(number, base, target)
    description = f"Vérification de l'entrée: {number} avec base {base.upper()} et base cible {target.upper()}"
    assert result == expected, f"Échec: {description}, obtenu: {result}, attendu: {expected}"

def test_check_if_valid_input():
    # Tests pour la base binaire
    assert_valid_input("1010", "bin", "hex", True)   # valide: binaire vers hexadécimal
    assert_valid_input("1012", "bin", "dec", False)  # invalide: 2 n'est pas un chiffre binaire
    assert_valid_input("1001", "bin", "bin", True)   # valide: binaire vers binaire
    assert_valid_input("110", "bin", "dec", True)    # valide: binaire vers décimal

    # Tests pour la base décimale
    assert_valid_input("123", "dec", "hex", True)    # valide: décimal vers hexadécimal
    assert_valid_input("-123", "dec", "bin", False)  # invalide: nombre négatif non autorisé
    assert_valid_input("456", "dec", "dec", True)    # valide: décimal vers décimal
    assert_valid_input("12.5", "dec", "hex", False)  # invalide: nombre non entier (flottant)

    # Tests pour la base hexadécimale
    assert_valid_input("A1B", "hex", "bin", True)    # valide: hexadécimal vers binaire
    assert_valid_input("G1", "hex", "dec", False)    # invalide: 'G' n'est pas un chiffre hexadécimal
    assert_valid_input("1F4", "hex", "hex", True)    # valide: hexadécimal vers hexadécimal
    assert_valid_input("2AF", "hex", "dec", True)    # valide: hexadécimal vers décimal

    # Cas limites
    assert_valid_input("0", "bin", "dec", True)      # valide: 0 est un nombre binaire valide
    assert_valid_input("0", "dec", "hex", True)      # valide: 0 est un nombre décimal valide
    assert_valid_input("0", "hex", "bin", True)      # valide: 0 est un nombre hexadécimal valide

    # Tests pour des bases invalides
    assert_valid_input("123", "xyz", "hex", False)   # invalide: base source inconnue
    assert_valid_input("123", "dec", "abc", False)   # invalide: base cible inconnue

    print("Tous les tests ont réussi!")

def assert_conversion(nmb, base, target_base, expected):
    result = converter(nmb, base, target_base)
    description = f"Conversion {base.upper()} vers {target_base.upper()} pour {nmb}"
    assert str(result) == str(expected), f"Échec: {description}, obtenu: {result}, attendu: {expected}"

def test_converter():
    assert_conversion("1010", "bin", "hex", "a")
    assert_conversion("1010", "bin", "dec", "10")
    assert_conversion("a", "hex", "bin", "1010")
    assert_conversion("a", "hex", "dec", "10")
    assert_conversion("10", "dec", "bin", "1010")
    assert_conversion("10", "dec", "hex", "a")
    assert_conversion("0", "dec", "bin", "0")
    assert_conversion("0", "dec", "hex", "0")
    assert_conversion("0", "bin", "dec", "0")
    assert_conversion("0", "hex", "dec", "0")

    print("Tous les tests ont réussi!")

# Appel de la fonction de test
test_converter()