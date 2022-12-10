import pygame

from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface
import sys

class pipe(Sprite):
    def __init__(self):
        self.sprite_image = "Blocks\pipe.png"
        self.sprite_width = 50
        self.sprite_height = 50
        self.sprite_sheet = pygame.image.load(self.sprite_image).convert()
        self.sprite_columns = 3
        self.current_frame = 0
        
        self.image = Surface((self.sprite_width, self.sprite_height))
 
        rect = (self.sprite_width*self.current_frame, 0,
                  self.sprite_width, self.sprite_height)

        self.image.blit(self.sprite_sheet, (0,0), rect)
        self.image.set_colorkey(Color(25, 25, 25))
        self.rect = self.image.get_rect()


    def update(self):
        if self.current_frame == self.sprite_columns -1:
            self.current_frame = 0
        else:
            self.current_frame += 1

        rect = (self.sprite_width*self.current_frame, 0,
                  self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet, (0,0), rect)
