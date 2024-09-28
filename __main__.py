import sys
import modules.ui as ui
import modules.tests as tests

#Detect le type de launch, si c'est ui, cmd simple ou module import
def detect_launch_type():
    args = sys.argv

    launch_type = 0 #Type de Lancement. 0 = UI, 1 = cmd mais sans la base de depart, 2 = cmd avec la base de depart., 3 = Tests

    if len(args) == 3:
        launch_type = 1
    elif len(args)>3:
        launch_type = 2

    if len(args) > 1:
        if args[1] == "run_test":
            launch_type = 3

    return launch_type

if __name__ == "__main__":
    launch = detect_launch_type()
    if launch == 0:
        number, base, target = ui.main()
        
    elif launch == 3:
        tests.run_tests()