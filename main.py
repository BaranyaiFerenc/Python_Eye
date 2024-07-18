#main file

from PIL import Image
import numpy as np

import datetime


def compare():
    first_time = datetime.datetime.now()


    img1 = Image.open('img1.PNG')
    img2 = Image.open('img2.PNG')

    sizeFactor = 4

    img1.thumbnail((int(img1.size[0] / sizeFactor), int(img1.size[1] / sizeFactor)))
    img2.thumbnail((int(img2.size[0] / sizeFactor), int(img2.size[1] / sizeFactor)))

    img1_matrix = np.array(img1)
    img2_matrix = np.array(img2)

    sizeX, sizeY = img1.size

    print("New size: "+str(sizeX)+"x"+str(sizeY))

    correct = 0 
    all = 0

    img = Image.new(mode="RGB", size=(sizeX, sizeY), color=(255, 255, 255))

    pixels = img.load()


    for x in range(0,sizeX):
        for y in range(0,sizeY):
            
            arr1 = img1_matrix[y][x]
            arr2 = img2_matrix[y][x]

            avgDiff = (abs(arr1[0]-arr2[0])+abs(arr1[1]-arr2[1])+abs(arr1[2]-arr2[2]))/3

            if  avgDiff == 0:
                correct+=1

            pixels[x,y] = (255,int(255-avgDiff),255)

            all += 1

    correctRatio = correct/all

    print("Correct: "+str(correctRatio))

    img.save("wrongIMG.png")

    later_time = datetime.datetime.now()
    difference = later_time - first_time
    datetime.timedelta(0, 8, 562000)
    seconds_in_day = 24 * 60 * 60
    divmod(difference.days * seconds_in_day + difference.seconds, 60)

    print(difference)


import time
#import msvcrt as m
#import pyautogui

import keyboard


def main():
    print("Star scanning")
    
    while(True):
        if keyboard.is_pressed('p'):
            print("hello")



if __name__ == "__main__": 
    main()