from pathlib import Path
import sys
import os

homedata = Path.home()
userdata = ""
musicdata = ""


if os.getenv("XDG_CONFIG_HOME"):
    userdata = Path(os.getenv("XDG_CONFIG_HOME")) / 'deemix'
elif os.getenv("APPDATA"):
    userdata = Path(os.getenv("APPDATA")) / "deemix"
elif sys.platform.startswith('darwin'):
    userdata = homedata / 'Library' / 'Application Support' / 'deemix'
else:
    userdata = homedata / '.config' / 'deemix'

if os.getenv("XDG_MUSIC_DIR"):
    musicdata = Path(os.getenv("XDG_MUSIC_DIR")) / "deemix Music"
elif os.name == 'nt':
    import winreg
    sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    music_guid = '{4BD8D571-6D19-48D3-BE97-422220080E43}'
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
        location = winreg.QueryValueEx(key, music_guid)[0]
    musicdata = Path(location) / "deemix Music"
else:
    musicdata = homedata / "Music" / "deemix Music"

def getHomeFolder():
    return homedata

def getConfigFolder():
    return userdata

def getMusicFolder():
    return musicdata
