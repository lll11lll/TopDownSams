import pygame as pg
from math import sqrt, atan2, pi



# INSTEAD OF CREATING THE ARC USING PYGAME.draw
# Create my own arc sprite and use that instead

# create an arc class?
# 

class Player(pg.sprite.Sprite): 
    def __init__(self, x, y, win):
        # Creation of player, and creating the rect with provide x and y
        self.survivor = pg.image.load('Survivor1/survivor1Hold.png')
        self.rect = self.survivor.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5 
        self.mouseX, self.mouseY = pg.mouse.get_pos()
        self.arc = pg.image.load('Arc2.png')
        self.arcRect = self.arc.get_rect()
        self.win = win



    def draw(self):
        # Drawing the sprite to the window
        self.win.blit(self.image, self.rect)
    

    def rotate(self):
    # Get mouse position and angles
        relativeX = self.mouseX - self.rect.x
        relativeY = self.mouseY - self.rect.y
        angle = ((180/pi)*-atan2(relativeY, relativeX))
        self.image = pg.transform.rotate(self.survivor, int(angle-90))
    
    def update(self):
        self.mouseX, self.mouseY = pg.mouse.get_pos()
        key = pg.key.get_pressed()

        #self.rect = self.image.get_rect()
        # Checking for key presses and moving the player accordingly
        # Checks if the player uses 2 keys at once and adjusts their speed to the same value as if they were only using 1 key
        # Up and Right
        if key[pg.K_w] and key[pg.K_d]:
            self.rect.x += (sqrt(12.5))
            self.rect.y -= (sqrt(12.5))
        
        # Up and Left
        elif key[pg.K_w] and key[pg.K_a]:
            self.rect.x -= (sqrt(12.5))
            self.rect.y -= (sqrt(12.5))
        
        # Down and Right
        elif key[pg.K_s] and key[pg.K_d]:
            self.rect.x += (sqrt(12.5))
            self.rect.y += (sqrt(12.5))
        # Down and Left
        elif key[pg.K_s] and key[pg.K_a]:
            self.rect.x -= (sqrt(12.5))
            self.rect.y += (sqrt(12.5))
        
        # Up
        elif key[pg.K_w]:
            self.rect.y -= self.speed

        # Down
        elif key[pg.K_a]:
            self.rect.x -= self.speed
        
        # Right
        elif key[pg.K_d]:
            self.rect.x += self.speed
        
        # Left
        elif key[pg.K_s]:
            self.rect.y += self.speed
        
        elif key[pg.K_SPACE]:
            # create arc from arc class
            self.arcRect.x = self.rect.x 
            self.arcRect.y = self.rect.y 
           
            self.win.blit(self.arc,  (self.arcRect.x, self.arcRect.y - self.survivor.get_height() ))
        
        self.rotate()