from gtts import gTTS
from gtts.tts import gTTSError
from os import system
from Json_Manip import json_manip

def create_audio(text : str , lang : str , accent : str, directory : str,fast : bool) -> str :
    try :
        lang = lang[:lang.index(" ")]
        text= text.strip()
        
        if text.__len__() == 0 :
            return ""
        x = gTTS(text=text,tld=accent,lang=lang,slow= not fast)
        path : str
        
        if directory.__len__() == 0 :
            path = "Audios/"
        else :
            path = directory+(text[:15].strip()+".mp3").replace(" ","_")

        try :
            x.save(path)
        except PermissionError :
            path = "Audios/tts_audio.mp3"
        except OSError:
            path = directory+"tts_audio.mp3"
        except :
            path = "Audios/tts_audio.mp3"
        x.save(path)

        play_cmd = json_manip.get_value("play_cmd")
        if play_cmd == "unknown" :
            return "This App is unable to detect your OS so the audio will not autoplay!\n\n  #> Succesfully save file : "+path
        
        try :
            system(play_cmd+" "+path)
        except :
            pass
        return "Succesfully saved file : "+path
    except ValueError as e :
        return "Value Error : "+e.__str__()  
    except AssertionError as e :
        return "Assertion Error : "+e.__str__()
    except RuntimeError as e :
        return "Runtime Error : "+e.__str__()
    except gTTSError as e :
        return "You are not connected to the Internet . : "
    return ""