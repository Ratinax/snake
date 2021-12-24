import pygame
from pygame.locals import *
from random import *
from time import *
from pages import*
pygame.init()
fen_x=1920
fen_y=int(16/9*fen_x)
fenetre = pygame.display.set_mode( (fen_x,fen_y), FULLSCREEN )
fenetre.fill((100,100,100))
pygame.display.flip()
page=pageDemarrage(fenetre,fen_x,fen_y)
continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=False
pygame.quit()