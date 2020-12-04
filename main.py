import os
import webbrowser

# Path to our folder that contains your app
path = str("/Users/kasper/Sites/")
projectFolders = list(os.listdir(path))

# Loop trough foldes
i = 0
while i < len(projectFolders):
    # Prints which index folder are.
    print projectFolders[i] + "[",i , "]"
    i += 1

# User choice
choice = raw_input('Which project will you work on?')

# Start mysql
os.system("mysql.server start")
# Open Browser
webbrowser.open('http://127.0.0.1:8000')
# Navigate to folder which user choices and Run php artisan serve
os.system( "cd " + path + projectFolders[int(choice)] + " && php artisan serve" )
