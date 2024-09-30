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

### ```Converter.py``` :

#### Fonctions de conversion

1. **`is_natural(c)`** : Vérifie si un caractère `c` est un nombre naturel (entier non négatif).

2. **`hex_to_dec(init_number)`** : Convertit un nombre en notation hexadécimale en décimal en utilisant une liste de coefficients hexadécimaux.

3. **`dec_to_hex(init_number)`** : Convertit un nombre décimal en notation hexadécimale.

4. **`dec_to_bin(init_number)`** : Convertit un nombre décimal en notation binaire.

5. **`bin_to_dec(init_number)`** : Convertit un nombre binaire en décimal.

### Validation d'entrée

6. **`check_if_valid_input(number, base, target)`** : Vérifie la validité de l'entrée (nombre, base d'origine, base cible) en s'assurant que les bases sont valides, que le nombre contient des caractères appropriés, et qu'il ne s'agit pas de valeurs incorrectes (comme des décimaux négatifs).

### Conversion générale

7. **`converter(init_number, init_base, target_base)`** : Fonction principale qui utilise les autres fonctions pour effectuer la conversion entre différentes bases (binaire, décimal, hexadécimal). Elle commence par vérifier la validité de l'entrée et effectue les conversions nécessaires.

### Logique de gestion des erreurs

Le code inclut des journaux d'erreurs pour gérer des entrées invalides et améliorer la robustesse du programme.
