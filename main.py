import pygame as pg
from settings import *

pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Top Down Shooter")
WIN = pg.display.set_mode((WIDTH, HEIGHT))


backgroundImage =  pg.transform.scale(pg.image.load('background.png'), (WIDTH, HEIGHT))

