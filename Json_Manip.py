from json import load,dump
from platform import system
class json_manip :

    @staticmethod
    def update_config(key: str, value: str | list):
        with open("_config_.json") as file:
            dit = load(file)
            dit[key] = value
            with open("_config_.json", "w") as file2:
                dump(dit, file2, indent=4)

    @staticmethod
    def get_value(key : str) :
        with open("_config_.json") as file :
            return load(file)[key]
        
    @staticmethod
    def OS_detected() :
        if not load(open("_config_.json"))["OS_checked"]:
            with open("_config_.json") as file :
                dit = load(file)
                if "windows" in system().lower() : dit["play_cmd"] = "start"
                elif "linux" in system().lower() : dit["play_cmd"] = "afplay"
                else : dit["play_cmd"] = "unknown"
                with open("_config_.json","w") as file2 :
                    dump(dit,file2,indent=4)
            json_manip.update_config("OS_checked",True)