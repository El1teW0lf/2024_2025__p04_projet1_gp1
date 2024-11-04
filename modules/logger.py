import time
from modules.data import DATA

lvl = 1
PREFIX = DATA().log["PREFIX"]

logfile = "logs.txt"

def LOG(data: str, level: int):
    current_time = time.localtime()  
    formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", current_time)

    log_msg = f"{formatted_time} [{PREFIX[level]}] {data}"
    
    if level >= lvl:
        print(log_msg)

    try:
        with open(logfile, "a") as file:
            pass
          
    except IOError as e:
        print(f"Error writing to log file: {e}")



