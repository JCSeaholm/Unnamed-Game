#provides OS info (screen size)
import tkinter
#allows user's settings to be saved in a JSON file to be retrieved later
import json
#allow's use to check the status of files
from os import stat

#the default screen width and height are determined by the actual screen's dimensions
root = tkinter.tk()
#dictionary to store screen settings
screen_settings = {
                   "screenWidth": root.winfo_screenwidth(), 
                   "screenHeight": root.winfo_screenheight()
                  }

#checks if the file in this path is empty
if os.stat("file").st_size == 0:
    #creates the userSettings.json file
    with open("userSettings.json", "w") as file:
        user_settings = json.load(file)
        json.dump(screen_settings, file, indent=2)
else:
    #use a JSON file to make it easier to save settings between sessions
    with open("userSettings.json") as file:
        user_settings = json.load(file)

#I'll have to mess with this, never used JSON beforel
userSetWidth = userSettings.width
userSetHeight = userSettings.height
