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

<h1 align="center"> 
   Ui.py :
</h1>

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

<h1 align="center"> 
   Tests.py :
</h1>

#### Importations et initialisation

- Le code importe des fonctions de conversion et de validation depuis les modules appropriés, ainsi que le module de journalisation.
- Il initialise des constantes pour les bases binaires, décimales et hexadécimales.

#### Fonctions de vérification et d'assertion

1. **`assert_valid_input(number, source_base, target_base, expected_result, error_counter)`** :
   - Vérifie si un nombre est valide pour les bases données.
   - Utilise `check_if_valid_input` et compare le résultat avec la valeur attendue.
   - Journalise le résultat et incrémente un compteur d'erreurs en cas d'échec.

2. **`assert_conversion(number, source_base, target_base, expected_result, error_counter)`** :
   - Vérifie si le résultat de la conversion d'un nombre entre bases est correct.
   - Utilise la fonction `converter` et compare le résultat avec la valeur attendue.
   - Journalise le résultat et incrémente un compteur d'erreurs en cas d'échec.

#### Tests de validation et de conversion

3. **`test_check_if_valid_input()`** :
   - Contient des cas de test pour valider les entrées en fonction de différentes bases.
   - Utilise `assert_valid_input` pour tester divers scénarios, y compris des cas de bords et des bases invalides.
   - Journalise le nombre total d'erreurs.

4. **`test_converter()`** :
   - Contient des cas de test pour vérifier les conversions entre différentes bases.
   - Utilise `assert_conversion` pour tester divers scénarios, y compris des conversions de zéro et des cas de bords.
   - Journalise le nombre total d'erreurs.

#### Fonction de lancement des tests

5. **`run_tests()`** :
   - Exécute les fonctions de test `test_converter` et `test_check_if_valid_input` pour valider l'ensemble du système de conversion.

<h1 align="center"> 
   Logger.py :
</h1>

#### Fonction de journalisation avancée
1. **Imports et initialisation** :
   - Le module `time` est utilisé pour récupérer et formater l'heure actuelle.
   - Les données de configuration (comme le préfixe de log) sont chargées à partir de `DATA()`.

2. **Variables** :
   - `current_time` : Récupère le temps local sous forme de structure de temps.
   - `formatted_time` : Formate la date et l'heure dans un format lisible (`jj/mm/aaaa hh:mm:ss`).
   - `lvl` : Définit le niveau de journalisation global (seulement les messages de niveau supérieur seront affichés).
   - `PREFIX` : Charge les préfixes associés aux niveaux de log.

3. **Fonction `LOG(data: str, level: int)`** :
   - Cette fonction affiche un message de log formaté avec la date, l'heure et un préfixe basé sur le niveau.
   - Si le niveau du message est inférieur au niveau global (`lvl`), le message n'est pas affiché.

#### Exemples de tests

Des exemples de tests sont proposés pour montrer comment la fonction `LOG` fonctionne :
- Les messages de niveau inférieur ou égal à `lvl` ne sont pas affichés.
- Les messages de niveau supérieur à `lvl` sont affichés.

<h1 align="center"> 
   Data.py :
</h1>

#### Classe `DATA`

La classe `DATA` sert à centraliser la gestion des données et des messages d'erreur pour un système de conversion de bases numériques. Elle contient plusieurs dictionnaires pour organiser les informations nécessaires.

#### 1. **Attributs de la classe**

- **`errors`** : Dictionnaire contenant des messages d'erreur associés à des clés spécifiques.
  - Exemples de clés : 
    - `"INVALID_START_BASE"` : Message pour une base d'initialisation invalide.
    - `"NOT_HEX_NUMBER"` : Message pour un nombre hexadécimal invalide.

- **`convert`** : Dictionnaire pour la gestion des conversions.
  - **`HEXA_MAP`** : Liste des caractères hexadécimaux de `0` à `f`.
  - **`BASES`** : Liste des bases disponibles : binaire (`bin`), décimal (`dec`), et hexadécimal (`hex`).

- **`ui`** : Dictionnaire contenant des informations pour l'interface utilisateur.
  - **`LOGO`** : Une chaîne ASCII représentant le logo.
  - **`COLOR_1` et `COLOR_2`** : Codes hexadécimaux pour des couleurs spécifiques.
  - **`COLORS`** : Liste de couleurs supplémentaires.
  - **`RANDOM_COLORS`** : Booléen indiquant si des couleurs aléatoires doivent être utilisées.
  - **`COLORED`** : Booléen pour activer/désactiver la coloration.
  - **`GRAD_STEP`** : Nombre de pas pour la génération de dégradés de couleur.

- **`test`** : Dictionnaire définissant des constantes pour les bases utilisées dans les tests.

#### 2. **Méthode `get_error`**

- **`get_error(self, error_key)`** :
  - Prend une clé d'erreur en entrée et retourne le message d'erreur correspondant depuis le dictionnaire `errors`.
  - Si la clé n'existe pas, elle retourne "Unknown error".

#### Utilisation

La classe `DATA` est conçue pour fournir une structure claire et accessible pour gérer les erreurs, les conversions et les paramètres d'interface utilisateur dans le cadre d'une application de conversion de bases. Cela permet de centraliser les messages et les constantes, facilitant ainsi la maintenance et l'évolution du code.

<h1 align="center"> 
   Keyboard :
</h1>

Le module `keyboard` est une bibliothèque Python qui permet de gérer les événements liés au clavier. Voici une description détaillée de ses fonctionnalités et de son utilisation :

#### Description détaillée

1. **Détection des touches** :
   - Permet de détecter quand une touche est pressée ou relâchée.
   - Utilisation de `keyboard.is_pressed('touche')` pour vérifier si une touche est actuellement enfoncée.

2. **Événements de clavier** :
   - Vous pouvez écouter des événements de clavier avec des fonctions comme `keyboard.on_press()` et `keyboard.on_release()`, qui vous permettent de définir des rappels (callbacks) qui s'exécutent lorsque des touches spécifiques sont pressées ou relâchées.

3. **Simulation de frappes** :
   - La fonction `keyboard.write()` permet de simuler la saisie de texte, tandis que `keyboard.press()` et `keyboard.release()` simulent l'appui et le relâchement de touches individuelles.

4. **Raccourcis clavier** :
   - Vous pouvez créer des raccourcis en utilisant `keyboard.add_hotkey('combinaison', fonction)` pour exécuter une fonction spécifiée lorsque la combinaison de touches est enfoncée.

5. **Enregistrement des frappes** :
   - Le module permet également d'enregistrer toutes les frappes au clavier, utile pour les applications de surveillance ou de diagnostic.

6. **Support multi-plateforme** :
   - Fonctionne sur Windows, macOS et certaines distributions Linux, bien que des permissions d'administrateur puissent être requises pour certaines fonctionnalités.

7. **Utilisation avancée** :
   - Possibilité de gérer des événements globaux (qui fonctionnent même si votre application n'est pas en avant-plan) et de configurer des délais ou des intervalles entre les frappes simulées.

#### Exemple de code

Voici un exemple de code montrant quelques-unes de ces fonctionnalités :

```Python
import keyboard

# Écouteur d'événements
def on_key_event(event):
    print(f'Touche {event.name} {event.event_type}')

keyboard.hook(on_key_event)

# Simuler l'appui sur une touche
keyboard.press('a')
keyboard.release('a')

# Ajouter un raccourci clavier
keyboard.add_hotkey('ctrl+c', lambda: print('Copié !'))

# Boucle principale
keyboard.wait('esc')  # Attendre que 'esc' soit pressé pour quitter
```
