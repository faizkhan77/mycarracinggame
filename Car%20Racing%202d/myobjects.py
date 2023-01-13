import pygame
import random

SCREEN = WIDTH, HEIGHT = 288, 512  # Display height and width


class Road():           # class for making 2 roads go in loop to give moving effect
    def __init__(self):
        self.image = pygame.image.load("Assets/road.png")       # loading & scaling road again
        self.image = pygame.transform.scale(self.image, (WIDTH-60, HEIGHT))

        self.reset()        
        self.move = True

    def update(self,speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed


            if self.y1 >= HEIGHT:
                self.y1 = -HEIGHT
            if self.y2 >= HEIGHT:
                self.y2 = -HEIGHT

    def draw(self, win):
        win.blit(self.image, (self.x, self.y1))
        win.blit(self.image,(self.x, self.y2))


    def reset(self):
        self.x = 30
        self.y1 = 0
        self.y2 = -HEIGHT

class player:
    def __init__(self, x, y, type): # x and y is position of car and type is type of selected car
        self.image = pygame.image.load(f"Assets/cars/{type+1}.png") # loading cars to select n storing in self.image
        self.image = pygame.transform.scale(self.image, (48, 82))   # resisizng cars sizes
        self.rect = self.image.get_rect()   # car movement in rectangle 
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right):   # for the car movement, left n right will be boolean so it dont go out of road
        if left:                # if left is true 
            self.rect.x -= 5      # then substract self.rect by 5
            if self.rect.x <= 40:
                self.rect.x = 40
        if right:               # else add by 5 if right is true
            self.rect.x += 5
            if self.rect.right >= 250:
                self.rect.right = 250

            

    def draw(self, win):    # displaying our car on screen
        win.blit(self.image, self.rect)

class Tree(pygame.sprite.Sprite):   # tree class
    def __init__(self, x, y):
        super(Tree,self).__init__()   
        type = random.randint(1, 4)     # placing trees at random place using random module
        self.image = pygame.image.load(f"Assets/trees/{type}.png")   # loading all treees image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed):
        self.rect.y += speed
        if self.rect.y >= HEIGHT:
            self.kill()

    def draw(self, win):
        win.blit(self.image, self.rect)