import time
from modules.data import DATA
import os

parent_directory = os.path.dirname(os.path.abspath(__file__))
lvl = 1
PREFIX = DATA().log["PREFIX"]

logfile = os.path.join(parent_directory,"logs.txt")

def LOG(data: str, level: int):
    current_time = time.localtime()  
    formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", current_time)

    log_msg = f"{formatted_time} [{PREFIX[level]}] {data}"
    
    if level >= lvl:
        print(log_msg)

    try:
        with open(logfile, "a") as file:
            file.write(log_msg+"\n")
          
    except Exception as e:
        print(f"Error writing to log file: {e}")



