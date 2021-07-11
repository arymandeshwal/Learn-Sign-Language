import cv2
from main_Hand_Tracking import cv2_handdetector
import pygame
import sys
from path_to_images import get_path_image
from matching_points import nearby
from get_alpha import get_current_alpha
import time

pygame.init()

def cvimage_to_pygame(image):
    """Convert cv2image into a pygame image"""
    return pygame.image.frombuffer(image.tobytes(), image.shape[1::-1],"RGB")

##def draw_connecting_lines(lmk):
##    for i in range(1,11,2):
##        pygame.draw.line(screen,Green,(lmk[i][1],lmk[i][2]),(lmk[i+1][1],lmk[i+1][2]),2)

## Size of window
size = width, height = 1080, 680

## Colors
White = (255,255,255)
Black = (0,0,0)
Cyan = (0,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)

## Points
a = [(739, 304),(628, 380),(591, 390),(544, 388),(493, 391)]
## Setting screen size
screen = pygame.display.set_mode(size)


## Creating webcam object
cap = cv2.VideoCapture(0)

paths=get_path_image("resized_colored_small")
middle_paths=get_path_image("resized-alphabets")
shadow_paths=get_path_image("resized_shadow_images")
current_path=0
current_image=paths[current_path]
current_middle_image=middle_paths[current_path]
current_shadow_image = shadow_paths[current_path]
while cap.isOpened():
    ## Conditions for pygame window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
##        if pygame.mouse.get_pressed()[0]:
##            print(pygame.mouse.get_pos())
##
##        if pygame.key.get_pressed()[pygame.K_RIGHT]:
##            if current_path<len(paths)-1:
##                current_path+=1
##                current_middle_image=middle_paths[current_path]
##                current_image=paths[current_path]
##                current_shadow_image = shadow_paths[current_path]

##        if pygame.key.get_pressed()[pygame.K_LEFT]:
##            if current_path>0:
##                current_path-=1
##                current_middle_image=middle_paths[current_path]
##                current_image=paths[current_path]
##                current_shadow_image = shadow_paths[current_path]
##                alpha_points.append(sub_list)
##                sub_list = [chr(65+current_path)]
##                print(alpha_points)
                #print(current_shadow_image)
                

    color = Yellow

    pygame.draw.line(screen,Cyan,[0,150],[1080,150],4)
    pygame.draw.line(screen,Cyan,[250,0],[250,150],4)
    pygame.draw.line(screen,Cyan,[830,0],[830,150],4)

    '''------------------------------------------------------------------------'''
    #TOP RIGHT IMAGE
    right_image=cv2.imread(current_image)
    right_image=cv2.resize(right_image,(249,149))
    right_image=cvimage_to_pygame(right_image)
    screen.blit(right_image,(833,0))

    #TOP middle IMAGE
    middle_image=cv2.imread(current_middle_image)
    middle_image=cv2.resize(middle_image,(249,149))
    middle_image=cvimage_to_pygame(middle_image)
    screen.blit(middle_image,(415,0))

    #MAIN IMAGE
    shadow_image=cv2.imread(current_shadow_image)
    shadow_image=cv2.resize(shadow_image,(640,480))
    shadow_image=cvimage_to_pygame(shadow_image)
    screen.blit(shadow_image,(220,175))
    
    #main_rect = pygame.Rect((220,175),(640,480))
    #pygame.draw.rect(screen,Black,main_rect)

    
    

    ## Getting image from webcam    
    success, img = cap.read()
    #print(img.shape)
    img = cv2.flip(img,1)
    lmk_list,original = cv2_handdetector(img)
    
    ## Coverting from BGR to RGB as pygame uses RGB
    img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    ## Resizing to fit on the corner of the screen
    img = cv2.resize(img, (249,149))

    image = cvimage_to_pygame(img)
    if lmk_list:
        #print(lmk_list)
        for i in lmk_list:
            pts = (i[1]+220,i[2]+175)
            pygame.draw.circle(screen,Red,pts,5,0)
            #testing distance logic
        if nearby(lmk_list,get_current_alpha(current_path),50):
            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() < start_time+2000:
                color = Green
                screen.fill(color)
                pygame.draw.line(screen,Cyan,[0,150],[1080,150],4)
                pygame.draw.line(screen,Cyan,[250,0],[250,150],4)
                pygame.draw.line(screen,Cyan,[830,0],[830,150],4)
                #display right tick image
                correct_image=cv2.imread("correct.png")
                correct_image=cv2.resize(correct_image,(640,480))
                correct_image=cvimage_to_pygame(correct_image)
                screen.blit(correct_image,(220,175))

                screen.blit(right_image,(833,0))
                screen.blit(middle_image,(415,0))
                screen.blit(image,(0,0))
                
                pygame.display.update()
            

            if current_path<len(paths)-1:
                current_path+=1
                current_middle_image=middle_paths[current_path]
                current_image=paths[current_path]
                current_shadow_image = shadow_paths[current_path]
##        print(get_current_alpha(current_path))
    
##        draw_connecting_lines(lmk_list)
    
    ## Drawing on screen
    screen.blit(image,(0,0))

    pygame.display.update()
    screen.fill(color)
cap.release()
    
