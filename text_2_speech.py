from gtts import gTTS
from gtts.tts import gTTSError
from os import system


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
        try :
            system("start "+path)
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

#print(create_audio("rom rom bhaiyo ...... system paadh denge", lang='hi : English' , accent= 'com' , directory="D:/New folder (4)/",fast= True))