import sys
import modules.ui as ui

#Detect le type de launch, si c'est ui, cmd simple ou module import
def detect_launch_type():
    args = sys.argv

    launch_type = 0 #Type de Lancement. 0 = UI, 1 = cmd mais sans la base de depart, 2 = cmd avec la base de depart.

    if len(args) == 3:
        launch_type = 1
    elif len(args)>3:
        launch_type = 2

    return launch_type

if __name__ == "__main__":
    launch = detect_launch_type()
    print(launch)
    if launch == 0:
        ui.main()