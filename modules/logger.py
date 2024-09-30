lvl = 1

def log (data: str, level: int):
    if level < lvl:
        pass
    else:  
        print(f"[log] {data} (LEVEL: {level})")

# Proposition par chatgpt du test du logger
#lvl = 1  # Définit le niveau global à 1 (seulement les messages de niveau > 1 seront affichés)
#log("This is a debug message.", 0)  # Rien ne s'affiche car le niveau est inférieur à lvl
#log("This is an info message.", 1)   # Rien ne s'affiche car le niveau est égal à lvl
#log("This is a warning message.", 2) # Ce message s'affiche car son niveau est supérieur à lvl