import sys
import time
import modules.tests as tests
import modules.converter as converter
import modules.data as Data
from modules.logger import LOG
import sys
from getpass import getpass
import subprocess
import pkg_resources
import modules.keyboard as keyboard

#Verifie si le modules "pynput", nécessaire est disponible

required = {'keyboard'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

data = Data.DATA()





#Detect le type de launch, si c'est ui, cmd simple ou module import
def detect_launch_type():
    args = sys.argv

    launch_type = 0 #Type de Lancement. 0 = UI,2 = cmd avec la base de depart., 3 = Tests

    if len(args) == 3:
        launch_type = 1
    elif len(args)>3:
        launch_type = 2

    if len(args) > 1:
        if args[1] == "run_test":
            launch_type = 3

    return launch_type

def run():
   
    LOG("Started BCONVERT",0)

    #assert len(missing) == 0, data.errors["MISSING_PACKAGES"]

    import modules.ui as ui
    
    launch = detect_launch_type()
    LOG(f"Got launch type: {launch}",0)
    if launch == 0:
        number, base, target = ui.main()
        result = ""
        mess = ""

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
                result, mess = converter.converter(number, data.convert["BASES"][base-1], data.convert["BASES"][target-1])
            except Exception as e:
                mess = str(e)
        print(result, mess)
        ui.main(result=result, error=mess, number=number, base=base, target=target)

    elif launch == 3:
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
                    raise Exception("Exited.")

