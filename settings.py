#allows user's settings to be saved in a JSON file to be retrieved later
import json

#use a JSON file to make it easier to save settings between sessions
userSettingsFile = open('userSettings.json', 'r')
userSettings = json.load(userSettingsFile)

#grabs the relevant data from the user input file
userSetWidth = userSettings["width"]
userSetHeight = userSettings["height"]
userSettingsFile.close()

#does the user want to change a setting? Use these.
def setWidth(width):
    userSettingsFile = open('userSettings.json', 'w')
    userSettings["width"] = width
    json.dump(userSettings, userSettingsFile)
    userSettingsFile.close()

def setHeight(height):
    userSettingsFile = open('userSettings.json', 'w')
    userSettings["height"] = height
    json.dump(userSettings, userSettingsFile)
    userSettingsFile.close()
