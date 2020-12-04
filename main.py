import os
import webbrowser

# Path to the folder that contains your apps
path = str("/Users/kasper/Sites/")
projectFolders = list(os.listdir(path))

# Loop through folders
i = 0
while i < len(projectFolders):
    # Prints folder name and index
    print projectFolders[i] + "[",i , "]"
    i += 1

# User choice
choice = raw_input('Which project will you work on?')
# Start mysql
os.system("mysql.server start")
# Open Browser
webbrowser.open('http://127.0.0.1:8000')
# Opens Atom
os.system("atom " + path + projectFolders[int(choice)])
# Navigate to folder, run php artisan serve
os.system( "cd " + path + projectFolders[int(choice)] + " && php artisan serve" )
