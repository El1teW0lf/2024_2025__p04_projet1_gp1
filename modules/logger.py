lvl = 0

def log (data: str, level: int):
    if level <= lvl:
        pass
    else:  
        print(f"[log] {data} (LEVEL: {level})")
