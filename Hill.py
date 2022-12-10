import pygame

from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

class Hill(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.init_image_change()
    
    def init_image_change(self):
        self.sprite_image = "Blocks\hill.png"
        self.sprite_width = 80
        self.sprite_height = 35
        self.sprite_sheet = pygame.image.load(self.sprite_image).convert()
        self.current_frame = 0
        
        self.image = Surface((self.sprite_width, self.sprite_height))

        rect = (self.sprite_width*self.current_frame, 0,
                  self.sprite_width, self.sprite_height)

        self.image.blit(self.sprite_sheet, (0,0), rect)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 255, 255))
        self.rect = self.image.get_rect()
        
    def image_change(self, img):
        self.sprite_image = img
        self.sprite_width = 80
        self.sprite_height = 35
        self.sprite_sheet = pygame.image.load(self.sprite_image).convert()
        self.current_frame = 0
        
        self.image = Surface((self.sprite_width, self.sprite_height))
        self.image.set_colorkey(Color(255, 255, 255))

        rect = (self.sprite_width*self.current_frame, 0,
                  self.sprite_width, self.sprite_height)

        self.image.blit(self.sprite_sheet, (0,0), rect)
        #self.rect = self.image.get_rect()
    
    def update(self):
        rect = (self.sprite_width*self.current_frame, 0,
                  self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet, (0,0), rect)

