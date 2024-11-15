import os
import math
from getpass import getpass
from modules.logger import LOG
from modules.data import DATA
import random
import modules.keyboard as keyboard
import threading
import time

data = DATA()

blank_char = " "

logo = data.ui["LOGO"]
color_1 = data.ui["COLOR_1"]
color_2 = data.ui["COLOR_2"]

menu_data = ""
fps = 10
lock = threading.Lock()

global_offset = 0
is_animated = data.ui["ANIMATED"]

global_data = []

is_rainbow = data.ui["RAINBOW"]
rainbow_size = data.ui["RAINBOW_DISTANCE"]

gradient_step = data.ui["GRAD_SPEED"]

def randomise_colors():

    global color_1
    global color_2

    if data.ui["RANDOM_COLORS"]:

        index_1 = random.randint(0,len(data.ui["COLORS"])-2)
        index_2 = index_1 + 1

        indices = [index_1, index_2]
        random.shuffle(indices)

        shuffled_index_1 = indices[0]
        shuffled_index_2 = indices[1]

        color_1 = data.ui["COLORS"][shuffled_index_1]
        color_2 = data.ui["COLORS"][shuffled_index_2]


randomise_colors()

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

        if is_rainbow:

            return center_text_width_from_other(
                apply_color_gradient(
                    text, generate_rainbow_gradient(steps=data.ui["GRAD_STEP"], offset=global_offset, distance=rainbow_size)
                ),
                text,
            )
        else:
            return center_text_width_from_other(
                apply_color_gradient(
                    text, generate_gradient(color1=color_1, color2=color_2, steps=data.ui["GRAD_STEP"], offset=global_offset)
                ),
                text,
            )
    else:
        return center_text_width_from_other(text, text)

def move_cursor(x, y):
    # ANSI escape sequence for cursor movement
    print(f"\033[{y};{x}H", end='')

# Function to hide/show the cursor
def hide_cursor(hide=True):
    print("\033[?25l" if hide else "\033[?25h", end='')



def hsv_to_rgb(h, s, v):
    h = h % 360  # Ensure hue is within 0-360 degrees
    c = v * s  # Chroma
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:  # 300 <= h < 360
        r, g, b = c, 0, x

    # Convert r, g, b to the range 0-255
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)

    return (r, g, b)

def rgb_to_hex(rgb):
    """Convert RGB color to hex color."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

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
def generate_gradient(color1: str, color2: str, steps: int, offset: int = 0):
    color1_rgb = hex_to_rgb(color1)
    color2_rgb = hex_to_rgb(color2)

    gradient = []

    for step in range(steps):
        adjusted_step = (step + offset) % steps
        interpolated_color = (
            int(color1_rgb[0] + (color2_rgb[0] - color1_rgb[0]) * adjusted_step / (steps - 1)),
            int(color1_rgb[1] + (color2_rgb[1] - color1_rgb[1]) * adjusted_step / (steps - 1)),
            int(color1_rgb[2] + (color2_rgb[2] - color1_rgb[2]) * adjusted_step / (steps - 1)),
        )
        gradient.append(rgb_to_hex(interpolated_color))

    return gradient

def generate_rainbow_gradient(steps: int, distance: int, offset: int = 0):

    gradient = []
    
    # Calculate hue increment based on the total distance and steps
    hue_increment = distance / steps
    
    for step in range(steps):
        # Calculate the current hue with offset
        hue = (offset + step * hue_increment) % 360
        # Convert the hue to RGB (assuming full saturation and value for a vibrant rainbow)
        rgb_color = hsv_to_rgb(hue, 1, 1)
        # Append the hex color to the gradient
        gradient.append(rgb_to_hex(rgb_color))
    
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


def print_menu(menu):
    # afficher ligne par ligne pour eviter le glitch du terminal qui panick
    # a la place de re print un gros block de la taille du terminal pour rafrachir l'ecran, on remplace ligne par ligne, ca marche mieux
    count = 0
    for line in menu.splitlines():
        move_cursor(0,count)
        print(line)
        count += 1

def get_menu_text(number: str = "", base: str = 0, target: str = 0, result: str = "", error: str = "", status: int = 0, from_signed: str = "", to_signed: str = ""):
    """Affiche le menu avec les informations saisies et les messages en fonction du statut.""" 

    menu_text = ""

    # Afficher le logo et le titre du projet
    menu_text += center_and_gradient(logo)
    menu_text += center_and_gradient(f"Groupe 1; Projet 1; Status: {status}")
    menu_text += line_skip(2)

    # Affichage du nombre source
    menu_text += display_status(f"Nombre Source: {number}", status, 0)

    # Affichage de la base de départ

    base_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base de départ: "
    menu_text += display_status(f"{base_prompt} {base}", status, 1)

    if base == "1" and status > 1:
    
        base_prompt = "[0: Non, 1: Oui] Binaire Signé ?: "
        menu_text += display_status(f"{base_prompt} {from_signed}", status, 2)

    # Affichage de la base d'arrivée
    target_prompt = "[1: Binaire, 2: Décimale, 3: Hexadécimal] Base d'arrivée: "
    menu_text += display_status(f"{target_prompt} {target}", status, 3)

    if target == "1" and status > 3:
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


    return menu_text
    




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


def update_display(number, base, target, status,from_signed,to_signed):
    global global_data
    global_data = [number,base, target, None,None,status,from_signed, to_signed]


def print_loop():
    while True:
        start_time = time.time()

        with lock:
            global global_offset
            if is_animated:
                global_offset += gradient_step
            data = global_data

        menu_data = get_menu_text(*data)    
        print_menu(menu_data)

        time.sleep(1 / fps)

        real_fps = 1 / (time.time() - start_time)
        
def input_loop(value, key_map, number, base, target, status,from_signed,to_signed):


    while True:
    
        if status == 0:
            update_display(value, base, target, status,from_signed,to_signed)  
        elif status == 1:
            update_display(number, value, target, status,from_signed,to_signed)  
        
        elif status == 2:
            update_display(number,base,target,status,value,to_signed)
        elif status == 3:
            update_display(number, base, value, status,from_signed,to_signed) 
        elif status == 4:
            update_display(number,base,target,status,from_signed,value)

        value, done = process_key_input(value, key_map)
        
        if done:
            return value

def get_input_live(number="", base="", target="", from_signed = "", to_signed = ""):    
    #clear()

    if number == "":
        number = input_loop(number, data.ui["COMPLETE_CHAT_MAP"], number, base, target, 0,from_signed,to_signed)
    
    if base == "":
        base = input_loop(base, data.ui["INT_CHAR_MAP"], number, base, target, 1,from_signed,to_signed)

    if base == "1" and from_signed == "":
        from_signed = input_loop(from_signed, data.ui["BOOL_CHAR_MAP"], number, base, target, 2,from_signed,to_signed)

    if target == "":
        target = input_loop(target, data.ui["INT_CHAR_MAP"], number, base, target,3,from_signed,to_signed)

    if target == "1" and to_signed == "":
        to_signed = input_loop(to_signed, data.ui["BOOL_CHAR_MAP"], number, base, target, 4,from_signed,to_signed)

    return number, base, target,from_signed,to_signed




def main(error=None, result=None, number=None, base=None, target=None,from_signed = None,to_signed = None):

    clear()
    hide_cursor(True)

    if error:
        display_error(error)
        return

    if result is None:
        number, base, target,from_signed,to_signed = collect_inputs()
        return number, base, target,from_signed,to_signed


    display_result(number, base, target, result)


def display_error(error):
    global global_data
    if error in data.errors:
        global_data = [None,None, None, None,data.errors[error],6,None, None]
    else:
        global_data = [None,None, None, None,f"Erreur Python: {error}",6,None, None]



def collect_inputs():
    number = base = target = from_signed = to_signed = ""
    LOG("Started input fetching.", 0)
    count = 0

    while not (number and base and target):
        number, base, target, from_signed, to_signed = get_input_live(number=number, target=target, base=base, from_signed=from_signed, to_signed=to_signed)
        count += 1

    return number, base, target, from_signed, to_signed


def display_result(number, base, target, result):
    back_up()
    global global_data
    global_data = [number,base, target, result,None,5,None, None]




def get_input(prompt, convert_to=str):
    """Helper function to get user input with optional conversion."""

    user_input = getpass(prompt)
    return convert_to(user_input)

def setup_loop():
    loop_thread = threading.Thread(target=print_loop)
    loop_thread.daemon = True 
    loop_thread.start()