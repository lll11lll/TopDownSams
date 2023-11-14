import pygame as pg
from settings import *
from player import *

pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Top Down Shooter")
WIN = pg.display.set_mode((WIDTH, HEIGHT))


backgroundImage =  pg.transform.scale(pg.image.load('background.png'), (WIDTH, HEIGHT))

def drawWindow(player):
    WIN.blit(backgroundImage, (0,0))
    player.update()
    player.draw(WIN)
    
    pg.display.update()


def main():
    player = Player(500, 375)
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        drawWindow(player)
main()