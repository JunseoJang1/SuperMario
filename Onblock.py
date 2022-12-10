import pygame
from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

class Onblock(Sprite):
    def __init__(self):
        super().__init__()

    def isonblock(self, me, other):
        me.rect.y -= 0.1
        collided = pygame.sprite.groupcollide(
            me, other, False, False)

        if collided:
            print(other, '과 부딫침!')
            if other.rect.bottom == Mario.rect.top:
                print(other, '의 아래, ', me, '의 top이 부딫침!')
