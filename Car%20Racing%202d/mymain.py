import pygame
import random
from myobjects import player, Road, Tree


pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512  # Display height and width

win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)  # Setting the Display

blue = (30, 144, 255)  # setting window color in rgb
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
green = (0, 255, 0)

# Loading images
home_image = pygame.image.load("Assets/home.png")   # Loading home image
bg_image = pygame.image.load("Assets/bg.png")   # Loading bacgkground image
road_image = pygame.image.load("Assets/road.png")   # Loading road image
road_image = pygame.transform.scale(road_image, (WIDTH-60, HEIGHT)) # resizing width n height of road image so it dont cover the entire bg imnage

# object
road = Road()
p = player(100, HEIGHT-120, 0)      # creating car object



tree_group = pygame.sprite.Group()

# Variables
home_page = False
game_page = True

move_left = False
move_right = False

counter = 0
speed = 3   # so car will move 3 px
running = True      # Creating an infinite running value to keep the game running
while running:
    win.fill(blue)       # filing in window color 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # if we click on the x on top it should quit
            running = False

        if event.type == pygame.KEYDOWN:    # checking events when a key is pressed
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: # if ESC or q is pressed game should stop
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:    
            x,y = event.pos
            
            if x <= WIDTH // 2:
                move_left == True
            else:
                move_right = True

        if event.type == pygame.MOUSEBUTTONUP:  # if no longer touching the surface then 
            move_left = False                   # more left & right gonna be False
            move_right = False                  # so it doesnt move automatically

        if home_page:
            win.blit(home_image, (0,0)) # putting the home image on screen with x and y cordinate set to 0,0
        if game_page:
            win.blit(bg_image, (0,0))   # putting bg image on screen
            road.update(speed)
            road.draw(win)


            counter += 1
            if counter % 60 == 0:
                tree = Tree(random.choice([-5, WIDTH-35]), -20)
                tree_group.add(tree)

        
            tree_group.update(speed)
            tree_group.draw(win)



            p.update(move_left, move_right)
            p.draw(win) # calling draw func from myobject.py

        pygame.display.update() # Every changes made gets updated from here

pygame.quit()