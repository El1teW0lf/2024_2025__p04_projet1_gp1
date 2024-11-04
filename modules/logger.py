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
<<<<<<< HEAD
           # file.write(log_msg +"\n")
           pass
=======
            pass
>>>>>>> c67897989a301a42af8462e2b9d7ae01cbc6b4c9
          
    except IOError as e:
        print(f"Error writing to log file: {e}")



