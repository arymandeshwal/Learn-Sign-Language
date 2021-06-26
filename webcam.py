import cv2
import pygame
pygame.init()

def cvimage_to_pygame(image):
    """Convert cv2image into a pygame image"""
    return pygame.image.frombuffer(image.tobytes(), image.shape[1::-1],"RGB")

## Size of window
size = width, height = 1080, 620

## Colors
White = (255,255,255)
Black = (0,0,0)
Cyan = (0,255,255)

## Setting screen size
screen = pygame.display.set_mode(size)

## Creating webcam object
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ## Conditions for pygame window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.draw.line(screen,Cyan,[0,150],[1080,150],4)
    pygame.draw.line(screen,Cyan,[250,0],[250,150],4)
    pygame.draw.line(screen,Cyan,[830,0],[830,150],4)
    

    ## Getting image from webcam    
    success, img = cap.read()
    ## Coverting from BGR to RGB as pygame uses RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ## Resizing to fit on the corner of the screen
    img = cv2.resize(img, (249,149))
    
    image = cvimage_to_pygame(img)
    ## Drawing on screen
    screen.blit(image,(0,0))

    pygame.display.update()
cap.release()
    
