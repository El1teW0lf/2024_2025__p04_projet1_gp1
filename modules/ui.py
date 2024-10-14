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

# Permet de recupere le texte pour le rendu du menu principal
def get_menu_text(number: str = "", base: str = 0, target: str = 0, result: str = "", error: str = "", status:int = 0):
    menu_text = ""

    menu_text += center_and_gradient(logo)
    menu_text += center_and_gradient("Groupe 1; Projet 1")
    menu_text += line_skip(2)

    # Affichage du nombre source
    menu_text += center_and_gradient(f"=> Nombre Source: {number}" if status == 0 else f"Nombre Source: {number}")

    # Affichage de la base de départ
    base_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base de départ: "
    menu_text += center_and_gradient(f"=> {base_prompt} {base}" if status == 1 else f"{base_prompt} {base}")


    base_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base d'arrivée: "
    menu_text += center_and_gradient(f"=> {base_prompt} {target}" if status == 2 else f"{base_prompt} {target}")

    # Affichage du résultat
    if status == 3:
        menu_text += line_skip(1)
        menu_text += center_and_gradient(f"=> Résultat: {result}")
 
    # Affichage de l'erreur
    if status == 4:
        menu_text += line_skip(1)
        menu_text += center_and_gradient(f"=> Erreur: {error}")
        

    # Finalisation et affichage du menu
    menu_text += line_skip(1)
    menu_text += center_and_gradient("[Entrée pour continuer.]")
    menu_text = center_text_height(menu_text)
    print(menu_text)

def get_input_live(number="", base="", target=""):
    # Assuming `back_up()` and `get_menu_text()` are defined elsewhere
    clear()
    back_up()
    get_menu_text(number=number, base=base, target=target)

    if number is "":
        number = ""

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'enter':
                    return (number, "", "")
                elif key == 'delete' or key == "backspace":
                    number = number[:-1]

                # Handle 'esc' key to exit the function
                elif key == 'esc':
                    raise Exception("Exited.")

                # Ignore special keys and control characters (e.g., shift, ctrl)
                elif key in data.ui["CHAR_MAP"]:
                                number += data.ui["CHAR_MAP"][key]  # Replace with corresponding number

                # Otherwise, add normal alphanumeric characters to the input
                elif len(key) == 1:
                    number += key

                # Call the display function to show the updated input
            back_up()
            get_menu_text(number=number, base="", target="", status=0)
    
    elif base == "":
        base = ""

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'enter':
                    return (number, base, "")
                elif key == 'delete' or key == "backspace":
                    base = base[:-1]

                # Handle 'esc' key to exit the function
                elif key == 'esc':
                    raise Exception("Exited.")

                # Ignore special keys and control characters (e.g., shift, ctrl)
                elif key in data.ui["CHAR_MAP"]:
                                base += data.ui["CHAR_MAP"][key]  # Replace with corresponding number

                # Call the display function to show the updated input
            back_up()
            get_menu_text(number=number, base=base, target="", status=1)
            
    elif target == "":
        target = ""

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'enter':
                    return (number, base, target)
                elif key == 'delete' or key == "backspace":
                    target = target[:-1]

                # Handle 'esc' key to exit the function
                elif key == 'esc':
                    raise Exception("Exited.")

                # Ignore special keys and control characters (e.g., shift, ctrl)
                elif key in data.ui["CHAR_MAP"]:
                                target += data.ui["CHAR_MAP"][key]  # Replace with corresponding number

                # Call the display function to show the updated input
            back_up()
            get_menu_text(number=number, base=base, target=target, status=2)
        



def main(error=None, result=None, number=None, base=None, target=None):
    clear()

    if error is not None:
        get_menu_text(error=data.errors[error], status=4)
        return

    if result is None:
        
        number = base = target = ""
        LOG("Started input fetching.",0)
        count = 0
        
        while number == "" or base == "" or target == "" :
        
        
            number,base,target = get_input_live(number=number,target=target,base=base)
            LOG(f"Got input number:{number}, target:{target}, base:{base} from iteration: {count}",0)
            
            count += 1


        return number, base, target
    else:
        back_up()
        get_menu_text(number=number, base=base, target=target, result=result, status=3)


def get_input(prompt, convert_to=str):
    """Helper function to get user input with optional conversion."""

    user_input = getpass(prompt)
    return convert_to(user_input)
