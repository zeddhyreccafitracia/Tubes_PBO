import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombie
import os


class Deadshooter:
    width = 850
    height = 500
    velo = 5

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont(None, 20)
        pygame.display.set_caption(" Dead Shooter ")
        self.bg = pygame.image.load("./assets/BG.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        self.is_running = True
        while self.is_running:
            pygame.time.delay(100)
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Playing", (255, 255, 255), 20, 20)
            Player().show(self.screen)
            Zombie().show(self.screen)

            # Event Keyboard
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and Player().coor[1] > 0:
                Player().coor[1] -= self.velo
            if keys[pygame.K_DOWN] and Player().coor[1] < 400:
                Player().coor[1] += self.velo
            if keys[pygame.K_LEFT] and Player().coor[0] > 0:
                Player().coor[0] -= self.velo
            if keys[pygame.K_RIGHT] and Player().coor[0] < 500:
                Player().coor[0] += self.velo
            Zombie().coor[0] -= self.velo

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.is_running = False
                        return

            pygame.display.update()

        pygame.quit()
        sys.exit()
