lvl = 0

def LOG (data: str, level: int):
    if level <= lvl:
        pass
    else:  
        print(f"[log] {data} (LEVEL: {level})")
