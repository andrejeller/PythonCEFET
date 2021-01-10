import pygame, sys
from pygame.locals import *

#inicio o pygame
pygame.init()

#inicia a janela
windowSurface = pygame.display.set_mode ((500,400),0,32)
pygame.display.set_caption('Jogo da Velha')

#inicia as cores utilizadas
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#inicia as fontes
basicFont = pygame.font.SysFont(None, 48)

#inicia o texto
text = basicFont.render('Jogo da Velha' , True, BLACK, GREEN)
textRect = text.get_rect()
textRect.midtop = windowSurface.get_rect().midtop

#desenha o fundo branco
windowSurface.fill(WHITE)

#desenha as linhas verticais
pygame.draw.line(windowSurface,  BLUE, (150, 100), (150, 300), 4)
pygame.draw.line(windowSurface,  BLUE, (350, 100), (350, 300), 4)

#desenha as linhas horizontais
pygame.draw.line(windowSurface,  BLUE, (150, 100), (150, 300), 4)
pygame.draw.line(windowSurface,  BLUE, (350, 100), (350, 300), 4)

#obtem um array de pixel da superficie
pixArray = pygame.PixelArray(windowSurface)
pixArray [480] [380] = BLACK
del pixArray

#desenha o texto na janela
windowSurface.blit(text, textRect)

#desenha a janela na tela
pygame.display.update()

#roda o loop do jogo
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 