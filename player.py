import pygame as pg

class Player(pg.sprite.Sprite): 
    def __init__(self, x, y):
        self.survivor = pg.image.load('Survivor1/survivor1Hold.png')
        self.rect = self.survivor.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, window):
        window.blit(self.survivor, self.rect)

