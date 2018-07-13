#allows user's settings to be saved in a JSON file to be retrieved later
import json
#module let's us see the stats of a file
import os

#opens the json file with read and write access type as "file"
#file is auto closed with with
with open('userSettings.json', 'r+') as file:
    #if the json file is new and empty
    if os.stat('userSettings.json').st_size == 0:
        #creates a new dictionary with default 16:9 width & height
        settings = {'dimensions': {'width': 1280, 'height': 720} }
        #with r+, file write/read position needs to be reset
        file.seek(0)
        #dumps the dict into the json file, with 2 indent for better formatting
        json.dump(settings, file, indent=2)
    file.seek(0)
    settings_file = json.load(file)
    #sets the width and height variable
    userSetWidth = settings_file['dimensions']['width']
    userSetHeight = settings_file['dimensions']['width']

#does the user want to change a setting? Use this.
def setDimensions(width, height):
    userSettingsFile = open('userSettings.json', 'w')
    userSettings = { 'dimensions': {'width': width, 'height': height} }
    json.dump(userSettings, userSettingsFile)
    userSettingsFile.close()
