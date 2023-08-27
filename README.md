# Audio Creator

Hello reader , so this a AI Audio Creator Project which uses Google Text-to-speech API and makes easy to make sounds in different languages with different accents .

# How to Run this :
  1. Install Python3 on your System.
  2. Install PyQt5, gtts & json module .
  3. Run the Audio_Creator.py file .

# Files Explain :
  1. Audio_Creator.py = this file is the main file which you need to execute to use this Project
  2. text_2_speech.py = this file is used by Audio_Creator.py script to create audios.
  3. _config_.json = this file keeps all the necessary values and data which is required for faster performance & startup of app .
  4. Json_Manip.py = this file is used by both above mentioned python script to write & read _config_.json .
  5. icon.png = as the name suggests, it's a icon file .

# Folder Explain :
  1. Audios = this folder is the default folder which is used to store all the generated audio files .
  2. CSS_files = this folder keeps all the CSS stylesheets required by Audio_Creator.py file to style UI .


#Problem
 > Window warning everytime when generating audio :
    If the address of file where your audio file is saved have spaces like this "D:\MY PROJECTS\AI Audio Creator" then this error will arise
    but it will not affect the generation of your audio.
    Actually , this problem arise due to Operating System because the audio file is autoplayed using terminal commands of OS like this : start Audios/tts_audio.mp3
    and when there is spaces so it will take the text before the second space as its full command and eventually this problem occurs.
    If you have any solution to this , then make changes in it.
