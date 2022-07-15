import json
from .Steam import SteamDoesExist
from .EpicGames import EpicDoesExist

async def FindLaunchers():
    return EpicDoesExist(), SteamDoesExist()

async def WritePath():
    if EpicDoesExist() == "Epic Games is Installed":
        with open("../conf/LauncherPaths.json", "w") as JSONFile:
            json.dump(EpicDoesExist[1], JSONFile)
