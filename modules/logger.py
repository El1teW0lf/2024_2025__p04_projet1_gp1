import time
from modules.data import DATA

lvl = 0
PREFIX = DATA().log["PREFIX"]

logfile = "logs.txt"

def LOG(data: str, level: int):
    current_time = time.localtime()  
    formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", current_time)

    log_msg = f"{formatted_time} [{PREFIX[level]}] {data}"
    
    try:
        with open(logfile, "a") as file:
            file.write(log_msg +"\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

    if level >= lvl:
        print(log_msg)


