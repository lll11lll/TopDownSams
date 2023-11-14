import pygame as pg
from math import sqrt

class Player(pg.sprite.Sprite): 
    def __init__(self, x, y):
        self.survivor = pg.image.load('Survivor1/survivor1Hold.png')
        self.rect = self.survivor.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5


    def draw(self, window):
        window.blit(self.survivor, self.rect)
    
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_w] and key[pg.K_d]:
            self.rect.x += (sqrt(12.5) + 1)
            self.rect.y -= (sqrt(12.5) + 1)
            print(self.rect.y)
            print(self.rect.x)
            
        elif key[pg.K_w]:
            self.rect.y -= self.speed
            print(self.rect.y)
            print(self.rect.x)
        elif key[pg.K_a]:
            self.rect.x -= self.speed

        elif key[pg.K_s]:
            self.rect.y += self.speed
        elif key[pg.K_d]:
            self.rect.x += self.speed
        
            
