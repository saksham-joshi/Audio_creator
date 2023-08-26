from platform import system
from json import load , dump

with open("_config_.json") as file :
    dit = load(file)

    if "windows" in system().lower() : dit["play_cmd"] = "start"
    elif "linux" in system().lower() : dit["play_cmd"] = "afplay"
    
    with open("_config_.json","w") as file2 :
        dump(dit,file2,indent=4)