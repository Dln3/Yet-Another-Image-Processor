# CMPT 120 Yet Another Image Processor
# Starter code for main.py
# Author(s): Leon Chen, Long Nguyen
# Date: Dec. 6, 2021
# Description: Image Processor

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame

pygame.init()

# list of system options
system = [
    "Q: Quit", "O: Open Image", "S: Save Current Image",
    "R: Reload Original Image"
]

# list of basic operation options
basic = [
    "1: Apply Red Filter", "2: Apply Green Filter", "3: Apply Blue Filter",
    "4: Apply Sepia Filter", "5: Apply Warm Filter", "6: Apply Cold Filter",
    "7: Switch to Advanced Functions"
]

# list of advanced operation options
advanced = [
    "1: Rotate Left", "2: Rotate Right", "3: Double Size", "4: Half Size",
    "5: Locate Fish", "6: Switch to Basic Functions"
]


# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("")  # an empty line
    menuString.append("Choose the following options:")
    menuString.append("")  # an empty line
    menuString += system
    menuString.append("")  # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha():  # check if the input is an alphabet
        # handle system functionalities
        if userInput == "O":
            print("Log: Doing system functionalities " + userInput)
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            # handle user cancelling open operation
            if not "/" in openFilename:
                cmpt120imageProjHelper.showInterface(
                    img,
                    "Open Image " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return img
            cmpt120imageProjHelper.showInterface(
                cmpt120imageProjHelper.getImage(openFilename),
                "Open Image " + openFilename.split("/")[-1],
                generateMenu(state))
            state["lastOpenFilename"] = openFilename
            return cmpt120imageProjHelper.getImage(openFilename)
        elif userInput == "S":
            print("Log: Doing system functionalities " + userInput)
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            # handle user cancelling save operation
            if not "/" in saveFilename:
                cmpt120imageProjHelper.showInterface(
                    img,
                    "Save Image " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return img
            cmpt120imageProjHelper.saveImage(img, saveFilename)
            state["lastSaveFilename"] = saveFilename
            if state["lastOpenFilename"] == "":  # check empty case
                cmpt120imageProjHelper.showInterface(img, "No Image",
                                                     generateMenu(state))
            else:
                cmpt120imageProjHelper.showInterface(
                    img, "Save Image " + saveFilename.split("/")[-1],
                    generateMenu(state))
        elif userInput == "R":
            print("Log: Doing system functionalities " + userInput)
            if state["lastOpenFilename"] == "":  # check empty case
                return img
            cmpt120imageProjHelper.showInterface(
                cmpt120imageProjHelper.getImage(state["lastOpenFilename"]),
                "Reload Image " + state["lastOpenFilename"].split("/")[-1],
                generateMenu(state))
            return cmpt120imageProjHelper.getImage(state["lastOpenFilename"])
        else:  # invalid letter input
            print("Log: Invalid Letter")

    # handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit():  # has to be a digit for manipulation options
        # handle manipulation functionalities for basic functions
        if state["mode"] == "basic":
            if userInput == "1":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applyRed(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Red Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "2":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applyGreen(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Green Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "3":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applyBlue(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Blue Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "4":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applySepia(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Sepia Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "5":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applyWarm(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Warm Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "6":
                print("Log: Performing " + basic[int(userInput) - 1])
                newImage = cmpt120imageManip.applyCold(img)
                cmpt120imageProjHelper.showInterface(
                    newImage, "Apply Cold Filter " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "7":
                print("Log: Performing " + basic[int(userInput) - 1])
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(
                    img, "Adavanced Mode " +
                    state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
            else:  # invalid number input
                print("Log: Invalid Number")
        # handle manipulation functionalities for advanced functions
        elif state["mode"] == "advanced":
            if userInput == "1":
                print("Log: Performing " + advanced[int(userInput) - 1])
                newImage = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProjHelper.showInterface(
                    newImage,
                    "Rotate Left " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "2":
                print("Log: Performing " + advanced[int(userInput) - 1])
                newImage = cmpt120imageManip.rotateRight(img)
                cmpt120imageProjHelper.showInterface(
                    newImage,
                    "Rotate Right " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "3":
                print("Log: Performing " + advanced[int(userInput) - 1])
                newImage = cmpt120imageManip.doubleSize(img)
                cmpt120imageProjHelper.showInterface(
                    newImage,
                    "Double Size " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "4":
                print("Log: Performing " + advanced[int(userInput) - 1])
                newImage = cmpt120imageManip.halfSize(img)
                cmpt120imageProjHelper.showInterface(
                    newImage,
                    "Half Size " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "5":
                print("Log: Performing " + advanced[int(userInput) - 1])
                newImage = cmpt120imageManip.locateFish(img)
                cmpt120imageProjHelper.showInterface(
                    newImage,
                    "Locate Fish " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
                return newImage
            elif userInput == "6":
                print("Log: Performing " + advanced[int(userInput) - 1])
                state["mode"] = "basic"
                cmpt120imageProjHelper.showInterface(
                    img,
                    "Basic Mode " + state["lastOpenFilename"].split("/")[-1],
                    generateMenu(state))
            else:  # invalid number input
                print("Log: Invalid Number")
    else:  # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img


# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
    "mode": "basic",
    "lastOpenFilename": "",
    "lastSaveFilename": "",
    "lastUserInput": ""
}

currentImg = cmpt120imageProjHelper.getBlackImage(
    300, 200)  # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(
    currentImg, "No Image",
    generateMenu(appStateValues))  # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT:  #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
