#!/usr/bin/python
"""
Backup Script - User input folder ou files to backup then choose the destination location to put the files 

[Time options included]

@PedroMagalhaes2020
"""
import pathlib
import os

from tkinter import Tk     # from tkinter import Tk 
from tkinter.filedialog import askdirectory
#from pip._internal import main as pipmain


def deleteConfigFile():
   if os.path.exists("ConfigLoc.txt"):
     os.remove("ConfigLoc.txt")
     print("*** File deleted !!! ***")
     main()
   else:
     print("The file does not exist")
     main()    

def firstMenu(optionEntry):
     switcher = {
         1: 'Teste',
         2: 'Teste',
         3:  "Teste",
         4:  "Teste",
         5:  deleteConfigFile(),
         6:  "Teste"
        }
     return switcher.get(optionEntry, "Invalid option")



def backupFolder():

    print("")
    #Tkinter - File Dialog
    Tk().withdraw() 
    dirName = askdirectory() # show an "Open" dialog box and return the path to the selected directory
    print(dirName)
    file = open("ConfigLoc.txt", "w+") # Add in the file and folder method
    file.write(dirName)

def createFileWithConfiguration(configLoc, fileBackup):
    #print(configLoc)
    #print(fileBackup)

    #MENU FILES OR FOLDER
    print("Files or Folder???")
    print("1 - Files")
    print("2 - Folder")

    opt2 = input

    file = open("ConfigLoc.txt", "w+") # Add in the file and folder method
    file.write(fileBackup)
    
    
    #Tkinter - File Dialog
    Tk().withdraw() 
    dirName = askdirectory() # show an "Open" dialog box and return the path to the selected directory
    print(dirName)

    return 0
# ------------------------------- File Explorer --------------------------------------
# ---------------------------------------------------------------------

def main():
    print("::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::")
    print("::: Backup Script 2020 :::")
    print(":::::@PedroMagalhaes::::::")
    print("::::::::::::::::::::::::::")
    print("")

    #install package for open file dialog
    #pipmain(['install', '--user', 'easygui'])

    file = pathlib.Path("ConfigLoc.txt")
    if file.exists():
        print("-----------------------\n")
        print("[Config file found !!!]")
        print("-----------------------\n")
        print("Choose the action: \n")
        print("1 - Backup All Files")
        print("2 - Change files to backup")
        print("3 - Change Time to sync")
        print("4 - See dev page")
        print("5 - Delete Config file")
        print("6 - Exit")
        optionFirstMenu = input("Option : ")
        firstMenu(optionFirstMenu)
        #print(optionFirstMenu)
    else:
        print("Backup Configuration not found, create a new one")
        
        filesLocation = input("Please insert your file or folder destination to backup: ")
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        createFileWithConfiguration(currentDirectory, filesLocation)


if __name__ == "__main__":
    main()

