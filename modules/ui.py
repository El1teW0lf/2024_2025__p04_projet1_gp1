import os
import math
from getpass import getpass


logo = """
██████╗  ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗
██╔══██╗██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   
██╔══██╗██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   
██████╔╝╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   
╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   
"""

color_1 = "ff99c8"
color_2 = "e4c1f9"



#Permet de 'clear' le terminal, de tout suprimer
def clear():
    print(chr(27) + "[2J")

#Détermine la taille sur l'ecran d'un text donné, avec la taille en ligne et en colone.
def get_text_bounding_box(text: str):

    lines = text.splitlines()

    height = len(lines)
    width = max(len(line) for line in lines) if lines else 0

    return width, height

#Retourne la taille du terminal dans lequel le code a été lancé, avec les lignes et les colones
def get_terminal_size():

    size = os.get_terminal_size()

    return size.columns, size.lines

def add_blank_to_text(text:str, number:int):
    return " " * number + text

#Centre le texte sur l'axe horizontale en fonction de sa taille et de la taille du terminal, accepte le multiligne
def center_text_width(text: str,half:int):

    lines = text.splitlines()

    result = ""

    for i in lines:

        result += add_blank_to_text(i,half)
        result += "\n"

    return result

#Meme fonction que center_text_width juste quelle celle ci utilise un autre texte comme reference, en cas de text colore pas exemple
def center_text_width_from_other(text: str,cleared:str = None):

    if cleared == None:
        cleared = text

    terminal_size = get_terminal_size()

    current_text_size = get_text_bounding_box(cleared)
    half_size_to_add = math.floor((terminal_size[0] - current_text_size[0])/2)
    
    return center_text_width(text=text,half=half_size_to_add)

#Permet simplement d'avoir le text formater representant un saut de ligne de number lignes.
def line_skip(number: int):
     return center_text_width_from_other(" ") * number


#Permet de centrer un texte sur l'axe verticale en fonction de sa taille et de la taille du terminal
def center_text_height(text: str):
    terminal_size = get_terminal_size()

    current_text_size = get_text_bounding_box(text)
    half_size_to_add = math.floor((terminal_size[1] - current_text_size[1])/2)
    text = text + line_skip(half_size_to_add) 

    return text

#Permet de colorer le text et de le centrer sans que les characters ANSI fasse n'importe quoi en gros
def center_and_gradient(text:str):
    return center_text_width_from_other(apply_color_gradient(text, generate_gradient(color1=color_1,color2=color_2,steps=5)),text)

# Permet de recupere le texte pour le rendu du menu principal, sans l'afficher, juste le texte.
def get_menu_text(number:str = "",base:int = 0):

    menu_text = ""

    menu_text += center_and_gradient(logo)
    menu_text += center_and_gradient("Groupe 1; Projet 1")
    menu_text += line_skip(2)
    menu_text += center_and_gradient("Nombre Source: "+number)
    menu_text += center_and_gradient("Base: "+str(base))

    menu_text = center_text_height(menu_text)

    print(menu_text)

# Je veux dire j'ai meme besoin d'expliquer cette fonction ?
def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')  # Retire le # au cas ou
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb

# Bon la aussi ca devrait faire sens comme fonction, le nom est asser explicite comme ca
def rgb_to_hex(rgb_color: str):
    return '{:02x}{:02x}{:02x}'.format(*rgb_color)


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
    
    for step in range(steps):
        interpolated_color = (
            int(color1_rgb[0] + (color2_rgb[0] - color1_rgb[0]) * step / (steps - 1)),
            int(color1_rgb[1] + (color2_rgb[1] - color1_rgb[1]) * step / (steps - 1)),
            int(color1_rgb[2] + (color2_rgb[2] - color1_rgb[2]) * step / (steps - 1))
        )
        gradient.append(rgb_to_hex(interpolated_color))
    
    return gradient


#Permet de diviser une string en une list de n mini string de meme longeur (plus ou moins)
def divide_string(s: str, n: int):
    length, part_size, remainder = len(s), len(s) // n, len(s) % n
    parts, start = [], 0
    for i in range(n):
        current_part_size = part_size + (1 if i < remainder else 0)
        parts.append(s[start:start + current_part_size])
        start += current_part_size
    return parts


#Permet de colorer une chaine de characters en suivant un degrade, supporte le multiligne
def apply_color_gradient(text:str,gradient:list):

    length = len(gradient)
    lines = text.splitlines()
    result = []


    for i in lines:

        result.append("")
        divided = divide_string(i,length)
        for a in range(len(divided)):
            result[len(result)-1] += get_colored_char(divided[a],gradient[a])

    final_text = ""

    for i in result:
        final_text += i
        final_text += "\n"

    return final_text



def main():
    clear()
    get_menu_text()
    number = getpass("")
    clear()
    get_menu_text(number=number)
    base = int(getpass(""))
    clear()
    get_menu_text(number=number,base=base)

main()