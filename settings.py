#provides OS info (screen size)
import tkinter
#allows user's settings to be saved in a JSON file to be retrieved later
import json

#the default screen width and height are determined by the actual screen's dimensions
root = tkinter.tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

#use a JSON file to make it easier to save settings between sessions
userSettingsFile = open('userSettings.json')
userSettings = json.load(userSettings)

#I'll have to mess with this, never used JSON before
userSetWidth = userSettings.width
userSetHeight = userSettings.height
