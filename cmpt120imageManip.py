# CMPT 120 Yet Another Image Processor
# Sotarter code for cmpt120imageManip.py
# Author(s): Leon Chen, Long Nguyen
# Date: Dec. 6, 2021
# Description: Image Processor

import cmpt120imageProjHelper


# apply red filter to 2d rgb array
# return new 2d rgb array
def applyRed(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            line.append([j[0], 0, 0])
        newPixels.append(line)
    return newPixels


# apply green filter to 2d rgb array
# return new 2d rgb array
def applyGreen(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            line.append([0, j[1], 0])
        newPixels.append(line)
    return newPixels


# apply blue filter to 2d rgb array
# return new 2d rgb array
def applyBlue(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            line.append([0, 0, j[2]])
        newPixels.append(line)
    return newPixels


# apply sepia filter to 2d rgb array
# return new 2d rgb array
def applySepia(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            sepiaRed = min((j[0] * .393) + (j[1] * .769) + (j[2] * .189), 255)
            sepiaGreen = min((j[0] * .349) + (j[1] * .686) + (j[2] * .168),
                             255)
            sepiaBlue = min((j[0] * .272) + (j[1] * .534) + (j[2] * .131), 255)
            line.append([sepiaRed, sepiaGreen, sepiaBlue])
        newPixels.append(line)
    return newPixels


# apply warm filter to 2d rgb array
# return new 2d rgb array
def applyWarm(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            if j[0] < 64:
                newRed = j[0] / 64 * 80
            elif j[0] >= 64 and j[0] < 128:
                newRed = (j[0] - 64) / (128 - 64) * (160 - 80) + 80
            else:
                newRed = (j[0] - 128) / (255 - 128) * (255 - 160) + 160
            if j[2] < 64:
                newBlue = j[2] / 64 * 50
            elif j[2] >= 64 and j[2] < 128:
                newBlue = (j[2] - 64) / (128 - 64) * (100 - 50) + 50
            else:
                newBlue = (j[2] - 128) / (255 - 128) * (255 - 100) + 100
            line.append([newRed, j[1], newBlue])
        newPixels.append(line)
    return newPixels


# apply cold filter to 2d rgb array
# return new 2d rgb array
def applyCold(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            if j[0] < 64:
                newRed = j[0] / 64 * 50
            elif j[0] >= 64 and j[0] < 128:
                newRed = (j[0] - 64) / (128 - 64) * (100 - 50) + 50
            else:
                newRed = (j[0] - 128) / (255 - 128) * (255 - 100) + 100
            if j[2] < 64:
                newBlue = j[2] / 64 * 80
            elif j[2] >= 64 and j[2] < 128:
                newBlue = (j[2] - 64) / (128 - 64) * (160 - 80) + 80
            else:
                newBlue = (j[2] - 128) / (255 - 128) * (255 - 160) + 160
            line.append([newRed, j[1], newBlue])
        newPixels.append(line)
    return newPixels


# invert rows and colums of 2d rgb array to rotate image to the left
# return new 2d rgb array
def rotateLeft(pixels):
    newPixels = []
    for i in range(len(pixels[0]) - 1, -1, -1):
        line = []
        for j in pixels:
            line.append(j[i])
        newPixels.append(line)
    return newPixels


# invert rows and colums of 2d rgb array to rotate image to the right
# return new 2d rgb array
def rotateRight(pixels):
    newPixels = []
    for i in range(len(pixels[0])):
        line = []
        for j in range(len(pixels) - 1, -1, -1):
            line.append(pixels[j][i])
        newPixels.append(line)
    return newPixels


# double the size of the image by duplicating 2d rgb array values
# return new 2d rgb array
def doubleSize(pixels):
    newPixels = []
    for i in pixels:
        line = []
        for j in i:
            line.append(j)
            line.append(j)
        newPixels.append(line)
        newPixels.append(line)
    return newPixels


# half the size of the image by taking the average color of every 4 pixels
# return new 2d rgb array
def halfSize(pixels):
    newPixels = []
    for i in range(0, len(pixels) - 1, 2):
        line = []
        for j in range(0, len(pixels[0]) - 1, 2):
            averageRed = (pixels[i][j][0] + pixels[i + 1][j][0] +
                          pixels[i][j + 1][0] + pixels[i + 1][j + 1][0]) / 4
            averageGreen = (pixels[i][j][1] + pixels[i + 1][j][1] +
                            pixels[i][j + 1][1] + pixels[i + 1][j + 1][1]) / 4
            averageBlue = (pixels[i][j][2] + pixels[i + 1][j][2] +
                           pixels[i][j + 1][2] + pixels[i + 1][j + 1][2]) / 4
            line.append([averageRed, averageGreen, averageBlue])
        newPixels.append(line)
    return newPixels


# locate the fish, then draw a green rectangle around the fish
# return new 2d rgb array
def locateFish(pixels):
    minHeight = len(pixels)
    minWidth = len(pixels[0])
    maxHeight = 0
    maxWidth = 0
    # find the boundaries of the fish and assign them to the variables above
    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            if isYellow(
                    cmpt120imageProjHelper.rgb_to_hsv(pixels[i][j][0],
                                                      pixels[i][j][1],
                                                      pixels[i][j][2])):
                if i > maxHeight:
                    maxHeight = i
                if j > maxWidth:
                    maxWidth = j
                if i < minHeight:
                    minHeight = i
                if j < minWidth:
                    minWidth = j
    newPixels = []
    # draw the rectangle around the fish
    for i in range(len(pixels)):
        line = []
        for j in range(len(pixels[0])):
            if ((i == maxHeight or i == minHeight) and j <= maxWidth and j >= minWidth) or \
            ((j == maxWidth or j == minWidth) and i <= maxHeight and i >= minHeight):
                line.append([0, 255, 0])
            else:
                line.append(pixels[i][j])
        newPixels.append(line)
    return newPixels


# input hsb value and return True if it is yellow
# otherwise, return False
def isYellow(input):
    if input[0] > 45 and input[0] < 75 and input[1] > 40 and input[2] > 50:
        return True
    return False
