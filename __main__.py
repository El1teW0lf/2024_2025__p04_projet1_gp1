import sys
import time
import modules.tests as tests
import modules.converter as converter
import modules.data as Data
from modules.logger import LOG
import modules.keyboard as keyboard
import modules.ui as ui
import os

def close_terminal():
    if sys.platform == "win32":  # Windows
        os.system("exit")
    elif sys.platform == "linux" or sys.platform == "darwin":  # Linux/Mac
        os.system("exit")
    else:
        print("Unsupported OS")

    os._exit(0)  


data = Data.DATA()

ui_loop_set = False

#Detect le type de launch, si c'est ui, cmd simple ou module import
def detect_launch_type():
    args = sys.argv

    launch_type = 0 

    if len(args) > 1:
        if args[1] == "run_test":
            launch_type = 3
        if args[1] == "help":
            launch_type = 3
        if args[1] == "set":
            launch_type = 3

    return launch_type

def run():
   
    LOG("Started BCONVERT",0)

    #assert len(missing) == 0, data.errors["MISSING_PACKAGES"
    
    launch = detect_launch_type()
    LOG(f"Got launch type: {launch}",0)
    if launch == 0:

        global ui_loop_set
        if not ui_loop_set:
            ui.setup_loop()
            ui_loop_set = True

        number, base, target,from_signed,to_signed = ui.main()
        result = ""
        mess = ""

        to_signed_bool = from_signed_bool = False

        if from_signed != "" and from_signed != "0" and from_signed != "1":
            LOG(data.get_error("INVALID_BIN_TYPE"), 3)
            mess = "INVALID_BIN_TYPE"
        else:
            from_signed_bool = False if from_signed == "" or from_signed == "0" else True if from_signed == "1" else False

        if to_signed != "" and to_signed != "0" and to_signed != "1":
            LOG(data.get_error("INVALID_BIN_TYPE"), 3)
            mess = "INVALID_BIN_TYPE"

        else:
            to_signed_bool = False if to_signed == "" or to_signed == "0" else True if to_signed == "1" else False


        if type(base) != int:
            LOG(data.get_error("INVALID_START_BASE"), 3)
            mess = "INVALID_START_BASE"

        base = int(base)

        if type(target) != int:
            LOG(data.get_error("INVALID_TARGET_BASE"), 3)
            mess = "INVALID_TARGET_BASE"

        target = int(target)

        if base < 0 or base > 3:
            LOG(data.get_error("INVALID_START_BASE"), 3)
            mess = "INVALID_START_BASE"
        elif target < 0 or target > 3:
            LOG(data.get_error("INVALID_TARGET_BASE"), 3)
            mess = "INVALID_TARGET_BASE"
        # Cette partie là c'est Blackbox AI parce que moi ça marchait pas et lui ça marchait
        else:
            try:
                result, mess = converter.converter(number, data.convert["BASES"][base-1], data.convert["BASES"][target-1], from_signed=from_signed_bool, to_signed=to_signed_bool)
            except Exception as e:
                mess = str(e)
        print(result, mess)
        ui.main(result=result, error=mess, number=number, base=base, target=target)

    elif launch == 3:
        print(data.ui["LOGO"])
        tests.run_tests()

if __name__ == "__main__":
    while True:
        run()
        time.sleep(0.5)
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'enter':
                    break
                elif key == 'esc':
                    close_terminal()
