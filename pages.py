import pygame
from pygame.locals import *
from random import *
from time import *
from random import randint
import keyboard
def position_carre(x1,x2,y1,y2):    #fonction retournant True si la souris se trouve entre les coordonées indiquées qui définissent un rectangle
    positionX_souris = pygame.mouse.get_pos()[0]
    positionY_souris = pygame.mouse.get_pos()[1]
    if positionX_souris>x1 and positionX_souris<x2 and positionY_souris>y1 and positionY_souris<y2:
        return True
    return False
class pageDemarrage:
    def __init__(self,fenetre,fen_x,fen_y):
        texte_moyen = pygame.font.Font(None, int(250)) # police moyenne
        texte_solo = texte_moyen.render("Solo",True,(20,20,20))
        texte_duo= texte_moyen.render("Duo",True,(20,20,20))
        continuer=True
        while continuer==True:
            pygame.mouse.set_visible(True) # pour faire disparaitre le curseur par defaut
            fenetre.fill((100,100,100))
            for event in pygame.event.get():
                if event.type==QUIT:
                    continuer=False
                    pygame.quit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        continuer=False
                        pygame.quit()
                if event.type==MOUSEBUTTONDOWN:
                    if position_carre(660,1260,600,745):
                        sous_page=pageSolo(fenetre,fen_x,fen_y)
                    elif position_carre(660,1260,800,945):
                        sous_page=pageDuo(fenetre,fen_x,fen_y)
            rectangle = pygame.draw.rect(fenetre,(255,255,255),(660,600,600,145))

            rectangle = pygame.draw.rect(fenetre,(255,255,255),(660,800,600,145))

            if position_carre(660,1260,600,745):
                rectangle = pygame.draw.rect(fenetre,(200,200,200),(660,600,600,145))
            if position_carre(660,1260,800,945):
                rectangle = pygame.draw.rect(fenetre,(200,200,200),(660,800,600,145))
            fenetre.blit(texte_solo,(660,600))
            fenetre.blit(texte_duo,(660,800))
            pygame.display.flip()
class pageSolo:
    def __init__(self,fenetre,fen_x,fen_y):
        pygame.mouse.set_visible(False) # pour faire disparaitre le curseur par defaut
        score=0
        texte_moyen = pygame.font.Font(None, int(100)) # police moyenne
        texte_gameover = texte_moyen.render("Game Over!",True,(220,220,220))
        texte_echap = texte_moyen.render("Clique sur échap pour quitter",True,(220,220,220))
        texte_score = texte_moyen.render(f"Score : {score}",True,(220,220,220))
        fenetre.fill((100,100,100))
        pygame.display.flip()
        continuer=True
        continuer2=True
        direction="haut"
        corps_snake=[[1000,400+i] for i in range(0,41,10)]
        point=False
        perte=True
        pause=False
        while continuer:
            while pause==True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        continuer=False
                        continuer2=False
                        pause=False
                    if event.type==KEYUP:
                        if event.key==K_ESCAPE:
                            continuer=False
                            continuer2=False
                            pause=False
                        if event.key==K_p:

                            pause=False
            if point==False:
                point=[10*randint(1,191),10*randint(1,107)]
            pygame.time.delay(35)
            for event in pygame.event.get():
                if event.type==QUIT:
                    continuer=False
                    continuer2=False
                if event.type==KEYUP:
                    if event.key==K_ESCAPE:
                        continuer=False
                        continuer2=False
                    if event.key==K_p:
                        if pause==False:
                            pause=True
                        else:
                            pause=False

            if keyboard.is_pressed('LEFT'):
                if direction!="droite":
                    direction="gauche"
            elif keyboard.is_pressed('RIGHT'):
                if direction!="gauche":
                    direction="droite"
            elif keyboard.is_pressed('UP'):
                if direction!="bas":
                    direction="haut"
            elif keyboard.is_pressed('DOWN'):
                if direction!="haut":
                    direction="bas"
            fenetre.fill((100,100,100))
            oui=0
            fenetre.blit(texte_score,(0,0))
            for partie in corps_snake:
                if corps_snake[0]==partie and oui!=0:
                    continuer=False
                    texte_gameover = texte_moyen.render(f"Game Over ! Votre score est de {score}",True,(220,220,220))
                rectangle = pygame.draw.rect(fenetre,(0,255,0),(partie[0],partie[1],10,10))
                oui+=1
            rectangle = pygame.draw.rect(fenetre,(255,0,0),(point[0],point[1],10,10))
            if corps_snake[0]==point:
                perte=False
                point=False
                score+=100
                texte_score = texte_moyen.render(f"Score : {score}",True,(220,220,220))
            elif corps_snake[0][0]<0 or corps_snake[0][0]>1910 or corps_snake[0][1]<0 or corps_snake[0][1]>1070:
                    texte_gameover = texte_moyen.render(f"Game Over ! Votre score est de {score}",True,(220,220,220))
                    continuer=False
            if direction=="gauche":
                corps_snake.insert(0,[corps_snake[0][0]-10,corps_snake[0][1]])
            elif direction=="droite":
                corps_snake.insert(0,[corps_snake[0][0]+10,corps_snake[0][1]])
            elif direction=="haut":
                corps_snake.insert(0,[corps_snake[0][0],corps_snake[0][1]-10])
            elif direction=="bas":
                corps_snake.insert(0,[corps_snake[0][0],corps_snake[0][1]+10])
            if perte==True:
                corps_snake.pop(len(corps_snake)-1)
            else:
                perte=True
            pygame.display.flip()
        while continuer2:
            for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key==K_ESCAPE:
                        continuer2=False
            fenetre.blit(texte_gameover,(50,200))
            fenetre.blit(texte_echap,(50,110))
            pygame.display.flip()
class pageDuo:
    def __init__(self,fenetre,fen_x,fen_y):
        pygame.mouse.set_visible(False) # pour faire disparaitre le curseur par defaut
        texte_moyen = pygame.font.Font(None, int(100)) # police moyenne
        texte_gameover = texte_moyen.render("Game Over!",True,(220,220,220))
        texte_echap = texte_moyen.render("Clique sur échap pour quitter",True,(220,220,220))
        fenetre.fill((100,100,100))
        pygame.display.flip()
        continuer=True
        continuer2=True
        direction="haut"
        direction2="haut"
        corps_snake=[[1000,400+i] for i in range(0,101,10)]
        corps_snake2=[[640,400+i] for i in range(0,101,10)]
        gagnant="égalité"
        point=False
        perte=True
        perte2=True
        pause=False
        while continuer:
            if point==False:
                point=[10*randint(1,191),10*randint(1,107)]
            while pause==True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        continuer=False
                        continuer2=False
                        pause=False
                    if event.type==KEYUP:
                        if event.key==K_ESCAPE:
                            continuer=False
                            continuer2=False
                            pause=False
                        if event.key==K_p:

                            pause=False
            pygame.time.delay(35)
            for event in pygame.event.get():
                if event.type==QUIT:
                    continuer=False
                    continuer2=False
                if event.type==KEYUP:
                    if event.key==K_ESCAPE:
                        continuer=False
                        continuer2=False
                    if event.key==K_p:

                        pause=True

            if keyboard.is_pressed('LEFT'):
                if direction!="droite":
                    direction="gauche"
            elif keyboard.is_pressed('RIGHT'):
                if direction!="gauche":
                    direction="droite"
            elif keyboard.is_pressed('UP'):
                if direction!="bas":
                    direction="haut"
            elif keyboard.is_pressed('DOWN'):
                if direction!="haut":
                    direction="bas"

            if keyboard.is_pressed('q'):
                if direction2!="droite":
                    direction2="gauche"
            elif keyboard.is_pressed('d'):
                if direction2!="gauche":
                    direction2="droite"
            elif keyboard.is_pressed('z'):
                if direction2!="bas":
                    direction2="haut"
            elif keyboard.is_pressed('s'):
                if direction2!="haut":
                    direction2="bas"



            fenetre.fill((100,100,100))
            oui=0
            for partie in corps_snake:
                if corps_snake[0]==partie and oui!=0:
                    gagnant="bleu"
                    continuer=False
                if corps_snake2[0]==partie:
                    if gagnant=="bleu":
                        gagnant="égalité"
                    else:
                        gagnant="vert"
                    continuer=False
                rectangle = pygame.draw.rect(fenetre,(0,255,0),(partie[0],partie[1],10,10))
                oui+=1

            oui=0
            for partie in corps_snake2:
                if corps_snake2[0]==partie and oui!=0:
                    gagnant="vert"
                    continuer=False
                if corps_snake[0]==partie:
                    if gagnant=="vert":
                        gagnant="égalité"
                    else:
                        gagnant="bleu"
                    continuer=False
                rectangle = pygame.draw.rect(fenetre,(0,0,255),(partie[0],partie[1],10,10))
                oui+=1

            rectangle = pygame.draw.rect(fenetre,(255,0,0),(point[0],point[1],10,10))
            if corps_snake[0]==point:
                perte=False
                point=False

            elif corps_snake[0][0]<0 or corps_snake[0][0]>1910 or corps_snake[0][1]<0 or corps_snake[0][1]>1070:
                gagnant="bleu"
                continuer=False

            if corps_snake2[0]==point:
                perte2=False
                point=False

            elif corps_snake2[0][0]<0 or corps_snake2[0][0]>1910 or corps_snake2[0][1]<0 or corps_snake2[0][1]>1070:
                if gagnant=="bleu":
                    gagnant="égalité"
                else:
                    gagnant="vert"

                continuer=False



            if direction=="gauche":
                corps_snake.insert(0,[corps_snake[0][0]-10,corps_snake[0][1]])
            elif direction=="droite":
                corps_snake.insert(0,[corps_snake[0][0]+10,corps_snake[0][1]])
            elif direction=="haut":
                corps_snake.insert(0,[corps_snake[0][0],corps_snake[0][1]-10])
            elif direction=="bas":
                corps_snake.insert(0,[corps_snake[0][0],corps_snake[0][1]+10])

            if direction2=="gauche":
                corps_snake2.insert(0,[corps_snake2[0][0]-10,corps_snake2[0][1]])
            elif direction2=="droite":
                corps_snake2.insert(0,[corps_snake2[0][0]+10,corps_snake2[0][1]])
            elif direction2=="haut":
                corps_snake2.insert(0,[corps_snake2[0][0],corps_snake2[0][1]-10])
            elif direction2=="bas":
                corps_snake2.insert(0,[corps_snake2[0][0],corps_snake2[0][1]+10])

            if perte==True:
                corps_snake.pop(len(corps_snake)-1)
            else:
                perte=True

            if perte2==True:
                corps_snake2.pop(len(corps_snake2)-1)
            else:
                perte2=True


            pygame.display.flip()
        while continuer2:
            if gagnant=="vert":
                texte_gameover = texte_moyen.render("Vert gagne !!",True,(0,255,0))
            elif gagnant=="bleu":
                texte_gameover = texte_moyen.render("Bleu gagne !!",True,(0,0,255))
            else:
                texte_gameover = texte_moyen.render("égalité.",True,(0,150,150))
            for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key==K_ESCAPE:
                        continuer2=False
            fenetre.blit(texte_gameover,(50,200))
            fenetre.blit(texte_echap,(50,110))
            pygame.display.flip()