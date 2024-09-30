<h1 align="center">
<img src="https://www.mediafire.com/file_premium/mnbpyuf9raqtih7/image-removebg-preview_%25283%2529.png/file">

  Projet de NSI n°1: Convertiseur de Base: BCONVERT

  <img src="http://ForTheBadge.com/images/badges/built-with-swag.svg">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg">
</h1>

# 👨‍💼 Membres :
### Classe de 1ere 4, Cours de Mr Pioche
* #### Célestin (GoldyRat)
* #### Mateo (El1teW0lf)
* #### Victor (Herasium)
* #### Benjamin (Ben-cpu-gpu)


# 🧮 BCONVERT :
### Ce programme vous permet de convertir vos nombres en :
* #### [Decimal](https://fr.wikipedia.org/wiki/Entier_naturel)
* #### [Binaire](https://fr.wikipedia.org/wiki/Binaire)
* #### [Hexadecimal](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal)
### Lancement du programme 💻 >>> ```__main__.py```
![Image](https://www.mediafire.com/file_premium/0pqfo96tqq1twgv/image.png/file)

# 🗂️ Fichiers :

* #### ```Converter.py ``` >>> Programme principal chargé de la converstion
* #### ```ui.py ``` >>> Programme destiné à l'interface de l'utilisateur
* #### ```tests.py ``` >>> Programme destiné au bon fonctionnement et à la détection d'erreur de Converter.py 
* #### ```logger.py ``` >>> Programme destiné à affficher à l'utilisateur l'erreur et son motif, et d'enregistrer pour les développeurs dans un ficher .txt 
* #### ```data.py ``` >>> Programme desitiné à la définition des fonctions tiers

# ⚙️ Fonctionnement :

<h1 align="center"> 
   Converter.py :
</h1>

#### Fonctions de conversion

1. **`is_natural(c)`** : Vérifie si un caractère `c` est un nombre naturel (entier non négatif).

2. **`hex_to_dec(init_number)`** : Convertit un nombre en notation hexadécimale en décimal en utilisant une liste de coefficients hexadécimaux.

3. **`dec_to_hex(init_number)`** : Convertit un nombre décimal en notation hexadécimale.

4. **`dec_to_bin(init_number)`** : Convertit un nombre décimal en notation binaire.

5. **`bin_to_dec(init_number)`** : Convertit un nombre binaire en décimal.

#### Validation d'entrée

6. **`check_if_valid_input(number, base, target)`** : Vérifie la validité de l'entrée (nombre, base d'origine, base cible) en s'assurant que les bases sont valides, que le nombre contient des caractères appropriés, et qu'il ne s'agit pas de valeurs incorrectes (comme des décimaux négatifs).

#### Conversion générale

7. **`converter(init_number, init_base, target_base)`** : Fonction principale qui utilise les autres fonctions pour effectuer la conversion entre différentes bases (binaire, décimal, hexadécimal). Elle commence par vérifier la validité de l'entrée et effectue les conversions nécessaires.

#### Logique de gestion des erreurs

Ce programme inclut des journaux d'erreurs pour gérer des entrées invalides et améliorer la robustesse du programme.

### ```ui.py``` :

#### Fonctions d'affichage et de mise en forme

1. **`clear()`** : Efface le terminal.

2. **`get_text_bounding_box(text: str)`** : Renvoie la largeur et la hauteur d'un texte donné.

3. **`get_terminal_size()`** : Retourne la taille actuelle du terminal (en colonnes et lignes).

4. **`add_blank_to_text(text: str, number: int)`** : Ajoute un certain nombre d'espaces devant un texte.

5. **`center_text_width(text: str, half: int)`** : Centre un texte horizontalement dans le terminal.

6. **`center_text_width_from_other(text: str, cleared: str = None)`** : Centre un texte horizontalement en utilisant un autre texte comme référence.

7. **`line_skip(number: int)`** : Génère des sauts de ligne formatés.

8. **`center_text_height(text: str)`** : Centre un texte verticalement dans le terminal.

9. **`center_and_gradient(text: str)`** : Centre un texte avec un dégradé de couleur si activé.

10. **`get_menu_text(number: str = "", base: int = 0, target: int = 0)`** : Génère et affiche le texte du menu principal en fonction des entrées fournies.

#### Fonctions de manipulation des couleurs

11. **`hex_to_rgb(hex_color: str)`** : Convertit une couleur hexadécimale en format RGB.

12. **`rgb_to_hex(rgb_color: str)`** : Convertit une couleur RGB en format hexadécimal.

13. **`get_colored_char(char: str, hex_color: str)`** : Applique une couleur à un caractère en utilisant les codes ANSI.

14. **`generate_gradient(color1: str, color2: str, steps: int)`** : Génère un dégradé de couleur entre deux couleurs hexadécimales.

15. **`divide_string(s: str, n: int)`** : Divise une chaîne en une liste de sous-chaînes de longueur similaire.

16. **`apply_color_gradient(text: str, gradient: list)`** : Applique un dégradé de couleur à un texte (supporte le multiligne).

#### Fonction principale

17. **`main()`** : Fonction principale qui gère le flux du programme, efface l'écran et demande à l'utilisateur de saisir des informations (nombre, base, cible) tout en mettant à jour l'affichage du menu.
