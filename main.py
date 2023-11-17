import pygame as pg
import sys
from settings import *
from player import *

pg.init()

clock = pg.time.Clock()  
pg.display.set_caption("Top Down Shooter")
WIN = pg.display.set_mode((WIDTH, HEIGHT))
     

backgroundImage =  pg.transform.scale(pg.image.load('background.png'), (WIDTH, HEIGHT))
   
def drawWindow(player):
    WIN.blit(backgroundImage, (0,0))

    # I think we should get rid of this image = player.rotate() and just have player.rotate() in the draw function of player.py,
    # It would create cleaner and more readable code
    #image = player.rotate()
    player.update() 
    player.draw()
    pg.display.update()


def main():
    player = Player(500, 375, WIN)
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        drawWindow(player)
main()