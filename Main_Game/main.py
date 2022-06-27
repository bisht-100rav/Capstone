# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:02:03 2022

@author: Saurav
"""

#Import tqdm and time from library
import time
from PIL import  Image
#from tqdm import tqdm

'''
#Simple progress bar
for i in tqdm(range(100)):
    time.sleep(0.03)
'''
#Importing pygame library as 'py'
import pygame as py

import random

#Initialisation of the pygame function
py.init()

# Assigning variables
# display height and width variables
display_width=800                   #Actually 'height'
display_height=400                  #Actually 'width'


#Assigning variables for colors to be used in game loop inside game
#Defining colors as RGB (255 by 255 by 255)
black = (0, 0, 0)
white = (255, 255, 255)
white_B = (230, 255, 255)
back = (108, 108, 108)
green_lime = (50, 205, 50)
green_forest = (34, 139, 34)
water_blue = (0, 135, 255)
water_blue_1 = (0, 135, 215)
water_blue_2 = (0, 135, 175)

#Setting up display using display.set_mode() function
gameDisplay = py.display.set_mode((display_width,display_height))

#Setting up title name for the game
py.display.set_caption('Dino Run 2.0')

#Assigning variable for the game_icon
game_icon = py.image.load("logo.png")
py.display.set_icon(game_icon)

#Global clock() function for gloabal variables
clock=py.time.Clock()

#Passing pause parameter as a global boolean to be used inside Pause_Menu()
pause = True

#Assigning global font
#If Sysfont() are not initialised then global font is to be taken by the function
font = py.font.SysFont("freesansbold.tff", 72)

'''
#Assigning Music and Sound Effects as variables
crash_sound=py.mixer.Sound('sound/Car_Crash.wav')
slide_sound=py.mixer.Sound('sound/Car_Slide.wav')
bonus_sound=py.mixer.Sound('sound/Car_Bonus.wav')
py.mixer.music.load('sound/Car_Moving.wav')
Game_intro_sound=py.mixer.Sound('sound/Game_Intro_Sound.wav')
Button_Press=py.mixer.Sound('sound/Button_Press.wav')
Pause_Menu_Sound=py.mixer.Sound('sound/Pause_Sound.wav')
'''


#Function for displaying Dino image
def Dino(x,y, img_count):
    scale = (120, 80)
    dino_imgs = [py.transform.scale(py.image.load("png/Run (1).png"),scale),
                 py.transform.scale(py.image.load("png/Run (2).png"),scale),
                 py.transform.scale(py.image.load("png/Run (3).png"),scale),
                 py.transform.scale(py.image.load("png/Run (4).png"),scale),
                 py.transform.scale(py.image.load("png/Run (5).png"),scale),
                 py.transform.scale(py.image.load("png/Run (6).png"),scale),
                 py.transform.scale(py.image.load("png/Run (7).png"),scale),
                 py.transform.scale(py.image.load("png/Run (8).png"),scale),
                 py.transform.scale(py.image.load("png/Run (1).png"),scale)]
    #blit draws over background
    imgs = dino_imgs[img_count]
    gameDisplay.blit(imgs, (x, y))

    
    
def Cloud(cloud_x, cloud_y):
    cloud_img = py.image.load('cloud.png')
    gameDisplay.blit(cloud_img, (cloud_x, cloud_y))


#Defining a function for game Exit to windows
def quit_game():
    py.quit()
    quit()


#Keeping the check of the score inside Text vairable
def Cars_Notcollided(count):
    font=py.font.SysFont(None,30)
    text = font.render("Score:"+str(count),True,black)
    gameDisplay.blit(text,(510,10))


#Main scene area for the game
def game_loop():
    time.sleep(1)
    global pause

    #Assinging variables for postion of objects/Sprites over the display area

    #Car_User posi
    img_count = 0
    x = (40)
    y = (300)
    x_change = 0
    y_change = 0
    
    
    # Cloud posi
    cloud_x = random.randrange(820, 1200)
    cloud_y = random.randrange(0, 40)
    cloud_speed = 10


    # Cloud posi
    cloud2_x = random.randrange(820, 1200)
    cloud2_y = random.randrange(40, 90)
    cloud2_speed = 10
    
    # Cloud posi
    cloud3_x = random.randrange(820, 1200)
    cloud3_y = random.randrange(90, 200)
    cloud3_speed = 10
    
    Exit=False

    while not Exit:

        #Event handling Loop for game checking for the keys being pressed
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type==py.KEYDOWN:
                if event.key==py.K_a:
                   x_change=-3.5
                if event.key==py.K_d:
                   x_change=3.5
                if event.key==py.K_w:
                    y_change=-1.98
                if event.key==py.K_s:
                    y_change=1.5
                if event.key==py.K_p:
                    pause = True
                    
            if event.type==py.KEYUP:
                if event.key==py.K_a or event.key==py.K_d:
                    x_change=0
            if event.type==py.KEYUP:
                if event.key==py.K_w or event.key==py.K_s:
                    y_change=0

        #Adding pos values to img variables of the Car_User
        x += x_change
        y += y_change

        #Calling of the Sprites as functions declared before loop
        #Layering is done as TOP to BOTTOM proprotionate to LOWER TO UPPER layer
        gameDisplay.fill(back)
        
        
        # Background display
        # base layer, background
        #py.draw.rect(gameDisplay,white,[0, 0, 800, 400])

        
        # Adding Sky
        py.draw.rect(gameDisplay, water_blue, [0, 0, 800, 220])
        py.draw.rect(gameDisplay, water_blue_1, [0, 400 - 280, 800, 480])
        py.draw.rect(gameDisplay, water_blue_2, [0, 400 - 180, 800, 200])
        
        # Adding layers
        # Ground
        py.draw.rect(gameDisplay, green_lime, [0, 400 - 10, 800, 10])
        py.draw.rect(gameDisplay, green_forest, [0, 400 - 20, 800, 10])
        py.draw.rect(gameDisplay, green_lime, [0, 400 - 30, 800, 10])
        py.draw.rect(gameDisplay, green_forest, [0, 400 - 40, 800, 10])
        py.draw.rect(gameDisplay, green_lime, [0, 400 - 50, 800, 10])
        py.draw.rect(gameDisplay, green_forest, [0, 400 - 60, 800, 10])
        py.draw.rect(gameDisplay, green_lime, [0, 400 - 70, 800, 10])
        py.draw.rect(gameDisplay, green_forest, [0, 400 - 80, 800, 10])
        
        
    
        Cloud(cloud_x, cloud_y)
        cloud_x -= cloud_speed
        
        Cloud(cloud2_x, cloud2_y)
        cloud2_x -= cloud2_speed
        
        Cloud(cloud3_x, cloud3_y)
        cloud3_x -= cloud3_speed
        
        
        Dino(x, y, img_count)
        img_count += 1
        
        # Looping clouds
        if cloud_x < -80:
            cloud_x = random.randrange(820, 1200)
            cloud_y = random.randrange(0, 40)
            
        if cloud2_x <- 80:
            cloud2_x = random.randrange(850, 1100)
            cloud2_y = random.randrange(40, 90)
            
        if cloud3_x <- 80:
            cloud3_x = random.randrange(840, 1800)
            cloud3_y = random.randrange(90, 200)
            
        if img_count == 9:
            img_count = 0

        # or py.display.flip() = updates entire surface
        py.display.update()
        clock.tick(64)


game_loop()
py.quit()
quit()