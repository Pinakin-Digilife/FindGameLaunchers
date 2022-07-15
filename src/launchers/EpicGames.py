import os
from ._sysinfo import sysplatform

def EpicDoesExist():
    try:
        if sysplatform() == "Windows":
            path = os.path.exists("C:/ProgramData/Epic/EpicGamesLauncher/Data/Manifests")
            EpicPath = {"path": "C:/ProgramData/Epic/EpicGamesLauncher/Data/Manifests"}
            return "Epic Games is Installed", EpicPath

        elif sysplatform() == "Linux":
            os.path.exists()

    except FileNotFoundError:
            return "Not Installed"



