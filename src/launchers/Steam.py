import os
from ._sysinfo import sysplatform


installpath = os.popen('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam" /v InstallPath').read().split()
installpath.remove("HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Valve\Steam")
installpath.remove("InstallPath"); installpath.remove("REG_SZ")

steamdir = installpath[0] + ' ' + installpath[1] + ' ' + installpath[2]

def SteamDoesExist():
    try:
        if sysplatform() == "Windows":
            os.path.exists(steamdir)
            return "Steam is Installed"

    except FileNotFoundError:
            return "Steam Not Installed"