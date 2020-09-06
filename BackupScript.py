#!/usr/bin/python
"""
Backup Script - User input folder ou files to backup then choose the destination location to put the files 

[Time options included]

@PedroMagalhaes2020
"""
import pathlib
import os

import tkinter as tk
from tkinter import filedialog
#from pip._internal import main as pipmain



def createFileWithConfiguration(configLoc, fileBackup):
    print(configLoc)
    print(fileBackup)
    file = open("ConfigLoc.txt", "w+")
    file.write(fileBackup)

    
    
    return 0

# ------------------------------- File Explorer --------------------------------------

# ---------------------------------------------------------------------


def main():

    print("::::::::::::::::::::::")
    print("::: Backup Script :::")
    print("::::::::::::::::::::::")
    print("\n")

    #install package for open file dialog
    #pipmain(['install', '--user', 'easygui'])

    file = pathlib.Path("LocFile.txt")
    if file.exists():
        print("Choose the action: ")
        print("1 - Backup All Files")
        print("2 - Change files to backup")
        print("3 - Change Time to sync")
        print("4 - See dev page")
        print("5 - Exit")
    else:
        print("Backup Configuration not found, create new one")
        filesLocation = input(
            "Please insert your file or folder location to backup: ")
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        createFileWithConfiguration(currentDirectory, filesLocation)


if __name__ == "__main__":
    main()

