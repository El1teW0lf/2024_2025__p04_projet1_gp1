import os
import math
from getpass import getpass
from modules.logger import LOG
from modules.data import DATA
import time
import random
import modules.keyboard as keyboard
import sys



data = DATA()

blank_char = " "

logo = data.ui["LOGO"]
color_1 = data.ui["COLOR_1"]
color_2 = data.ui["COLOR_2"]

if data.ui["RANDOM_COLORS"]:
    color_1 = random.choice(data.ui["COLORS"])
    color_2 = random.choice(data.ui["COLORS"])

colored = data.ui["COLORED"]


# Permet de 'clear' le terminal, de tout suprimer
def back_up():
 print("\033[H", end="") 

def clear():
  print(chr(27) + "[2J")
 

# Détermine la taille sur l'ecran d'un text donné, avec la taille en ligne et en colone.
def get_text_bounding_box(text: str):
    lines = text.splitlines()

    height = len(lines)
    width = max(len(line) for line in lines) if lines else 0

    return width, height


# Retourne la taille du terminal dans lequel le code a été lancé, avec les lignes et les colones
def get_terminal_size():
    size = os.get_terminal_size()

    return size.columns, size.lines


def add_blank_to_text(text: str, number: int,total: int = None):

    if total == None: total = number * 2
    return blank_char * number + text + blank_char * (total - number)


# Centre le texte sur l'axe horizontale en fonction de sa taille et de la taille du terminal, accepte le multiligne
def center_text_width(text: str, half: int, total: int):
    lines = text.splitlines()

    result = ""

    for i in lines:
        result += add_blank_to_text(i, half, total=total)
        result += "\n"

    return result


# Meme fonction que center_text_width juste quelle celle ci utilise un autre texte comme reference, en cas de text colore pas exemple
def center_text_width_from_other(text: str, cleared: str = None):
    if cleared == None:
        cleared = text

    terminal_size = get_terminal_size()

    current_text_size = get_text_bounding_box(cleared)
    half_size_to_add = math.floor((terminal_size[0] - current_text_size[0]) / 2)

    return center_text_width(text=text, half=half_size_to_add, total=terminal_size[0]- current_text_size[0])


# Permet simplement d'avoir le text formater representant un saut de ligne de number lignes.
def line_skip(number: int):
    return center_text_width_from_other(blank_char) * number


# Permet de centrer un texte sur l'axe verticale en fonction de sa taille et de la taille du terminal
def center_text_height(text: str):
    terminal_size = get_terminal_size()

    current_text_size = get_text_bounding_box(text)
    half_size_to_add = math.floor((terminal_size[1] - current_text_size[1]) / 2)
    text = line_skip(half_size_to_add) + text + line_skip(half_size_to_add)

    return text


# Permet de colorer le text et de le centrer sans que les characters ANSI fasse n'importe quoi en gros
def center_and_gradient(text: str):
    if colored:
        return center_text_width_from_other(
            apply_color_gradient(
                text, generate_gradient(color1=color_1, color2=color_2, steps=data.ui["GRAD_STEP"])
            ),
            text,
        )
    else:
        return center_text_width_from_other(text, text)






# Je veux dire j'ai meme besoin d'expliquer cette fonction ?
def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")  # Retire le # au cas ou
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return rgb


# Bon la aussi ca devrait faire sens comme fonction, le nom est asser explicite comme ca
def rgb_to_hex(rgb_color: str):
    return "{:02x}{:02x}{:02x}".format(*rgb_color)


# CHATGPT, je vais lui faire confiance sur celle la vu que bon hein j'y connais rien en ANSI escape code
# mais en tt cas ca a l'air de marcher
# Permet de prendre un character ou une chaine de character et de la colorer en fonction de la couleur donnée.
def get_colored_char(char: str, hex_color: str):
    rgb = hex_to_rgb(hex_color)
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{char}\033[0m"


# Permet de generer un degrade de couleur pour faire jolie sur le logo
def generate_gradient(color1: str, color2: str, steps: int):
    color1_rgb = hex_to_rgb(color1)
    color2_rgb = hex_to_rgb(color2)

    gradient = []

    for step in range(
        steps
    ):  # Pour faire simple cette boucle fait la moyenne entre deux couleurs pour en deduire un degrade genre 0 - 10 puis 0 - 5 - 10 puis 0 - 2.5 - 5 - 7.5 - 10
        interpolated_color = (
            int(color1_rgb[0] + (color2_rgb[0] - color1_rgb[0]) * step / (steps - 1)),
            int(color1_rgb[1] + (color2_rgb[1] - color1_rgb[1]) * step / (steps - 1)),
            int(color1_rgb[2] + (color2_rgb[2] - color1_rgb[2]) * step / (steps - 1)),
        )
        gradient.append(rgb_to_hex(interpolated_color))

    return gradient


# Permet de diviser une string en une list de n mini string de meme longeur (plus ou moins)
def divide_string(s: str, n: int):
    length, part_size, remainder = len(s), len(s) // n, len(s) % n
    parts, start = [], 0
    for i in range(n):
        current_part_size = part_size + (1 if i < remainder else 0)
        parts.append(s[start : start + current_part_size])
        start += current_part_size
    return parts


# Permet de colorer une chaine de characters en suivant un degrade, supporte le multiligne
def apply_color_gradient(text: str, gradient: list):
    length = len(gradient)
    lines = text.splitlines()
    result = []

    for i in lines:
        result.append("")
        divided = divide_string(i, length)
        for a in range(len(divided)):
            result[len(result) - 1] += get_colored_char(divided[a], gradient[a])

    final_text = ""

    for i in result:
        final_text += i
        final_text += "\n"

    return final_text


def display_status(text: str, current_status: int, target_status: int) -> str:
    """Affiche le texte avec une flèche si le statut correspond."""
    return center_and_gradient(f"=> {text}" if current_status == target_status else text)

# Permet de recupere le texte pour le rendu du menu principal
def get_menu_text(number: str = "", base: str = 0, target: str = 0, result: str = "", error: str = "", status: int = 0, from_signed: str = "", to_signed: str = ""):
    """Affiche le menu avec les informations saisies et les messages en fonction du statut."""
    
    menu_text = ""

    # Afficher le logo et le titre du projet
    menu_text += center_and_gradient(logo)
    menu_text += center_and_gradient("Groupe 1; Projet 1")
    menu_text += line_skip(2)

    # Affichage du nombre source
    menu_text += display_status(f"Nombre Source: {number}", status, 0)

    # Affichage de la base de départ

    base_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base de départ: "
    menu_text += display_status(f"{base_prompt} {base}", status, 1)

    if from_signed != "":
        base_prompt = "[0: Non, 1: Oui] Binaire Signé ?: "
        menu_text += display_status(f"{base_prompt} {from_signed}", status, 2)

    # Affichage de la base d'arrivée
    target_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base d'arrivée: "
    menu_text += display_status(f"{target_prompt} {target}", status, 3)

    if to_signed != "":
        base_prompt = "[0: Non, 1: Oui] Binaire Signé ?: "
        menu_text += display_status(f"{base_prompt} {to_signed}", status, 4)

    # Affichage du résultat si status = 3
    if status == 5:
        menu_text += line_skip(1)
        menu_text += center_and_gradient(f"=> Résultat: {result}")
        menu_text += line_skip(1)
        menu_text += center_and_gradient("Appuyez sur [Entrée] pour recommencer ou [Esc] pour quitter.")
    
    # Affichage de l'erreur si status = 4
    elif status == 6:
        menu_text += line_skip(1)
        menu_text += center_and_gradient(f"=> Erreur: {error}")
        menu_text += line_skip(1)
        menu_text += center_and_gradient("Appuyez sur [Entrée] pour recommencer ou [Esc] pour quitter.")

    # Sinon, finalisation du menu par défaut
    else:
        menu_text += line_skip(1)
        menu_text += center_and_gradient("[Entrée pour continuer.]")

    # Centrer le texte sur la hauteur et afficher
    menu_text = center_text_height(menu_text)
    print(menu_text)




def process_key_input(value, key_map):
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        if key == 'enter':
            return value, True  # Retourner la valeur et signaler la fin de la saisie
        elif key in ['delete', 'backspace']:
            value = value[:-1]  # Supprimer le dernier caractère
        elif key == 'esc':
            raise Exception("Exited.")  
        elif key in key_map:
            value += key_map[key]  # Ajouter le caractère correspondant
    return value, False


def update_display(number, base, target, status):
    back_up()
    get_menu_text(number=number, base=base, target=target, status=status)


def input_loop(value, key_map, number, base, target, status):
    while True:

        if status == 0:
            update_display(value, base, target, status)  
        elif status == 1:
            update_display(number, value, target, status)  
        elif status == 3:
            update_display(number, base, value, status) 

        value, done = process_key_input(value, key_map)

        if done:
            return value

def get_input_live(number="", base="", target=""):    
    clear()

    if number == "":
        number = input_loop(number, data.ui["COMPLETE_CHAT_MAP"], number, base, target, 0)
    
    if base == "":
        base = input_loop(base, data.ui["INT_CHAR_MAP"], number, base, target, 1)

    if target == "":
        target = input_loop(target, data.ui["INT_CHAR_MAP"], number, base, target,3)

    return number, base, target




def main(error=None, result=None, number=None, base=None, target=None):

    clear()

    if error:
        display_error(error)
        return

    if result is None:
        number, base, target = collect_inputs()
        return number, base, target


    display_result(number, base, target, result)


def display_error(error):
    if error in data.errors:
        get_menu_text(error=data.errors[error], status=6)
    else:
        get_menu_text(error=f"Erreur Python: {error}", status=6)


def collect_inputs():
    number = base = target = ""
    LOG("Started input fetching.", 0)
    count = 0

    while not (number and base and target):
        number, base, target = get_input_live(number=number, target=target, base=base)
        LOG(f"Got input number:{number}, target:{target}, base:{base} from iteration: {count}", 0)
        count += 1

    return number, base, target


def display_result(number, base, target, result):
    back_up()
    get_menu_text(number=number, base=base, target=target, result=result, status=5)



def get_input(prompt, convert_to=str):
    """Helper function to get user input with optional conversion."""

    user_input = getpass(prompt)
    return convert_to(user_input)
