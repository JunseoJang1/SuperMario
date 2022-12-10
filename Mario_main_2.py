import pygame

from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

from Mario import Player
from Pipe import pipe
from question_mark import Question
from cracked_brick import Cracked_Brick
from Hill import Hill
from const import *

q_list = ['platform-q.png', 'platform-q1.png', 'platform-q2.png', 'platform-q3.png']
s_list = ['mario1', 'mario2', 'mario3', 'mario4', 'mario5']
BLOCKRECT_LIST = [345, 327, 300, 277, 254]


vel = 5
jump = False
jumpCount = 0
jumpMax = 15

if __name__ == "__main__":

    ############# 초기 변수 설정 #############
    FPS = 60

    size = (400, 361)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Super Mario Bros. 1")
     
    background_img_menu = pygame.image.load("Background\Mario_menu.png")
    background_img_game = pygame.image.load("Background\Mario_sky.png")
    background_img = background_img_menu


    MarioPosition = 323
    Mario_dash = 0
    collided_block = 0
    collided_q1 = 0
    collided_qq = 0
    changeMario = 0

    rect_x = 0
    rect_xx = 0
    rect_xxx = 276

    cb_list = [300, 277, 254, 231, 208]
    cb_listy = [300, 277, 254, 231, 208]
    nextlevel = 0
    
    ############ 게임 안에 Sprites 설정 ##############
            
    cracked_brick_group = pygame.sprite.Group()
    Mario = Player()
    Mario.rect.x = -500
    Mario.rect.y = 295
    Mario_group = pygame.sprite.Group()
    Mario_group.add(Mario)

    Pipe = pipe()
    Pipe.rect.x = 100
    Pipe.rect.y = 295
    Pipe_group = pygame.sprite.Group()
    Pipe_group.add(Pipe)

    tmp_rect_y = 208
    tmp_rect_x = 0

    for i in range (20):
        cb = Cracked_Brick()
        cb.rect.x = rect_x
        cb.rect.y = 323
        cracked_brick_group.add(cb)
        rect_x += 23

    for k in range (20):
        cb = Cracked_Brick()
        cb.rect.x = rect_xx
        cb.rect.y = 345
        cracked_brick_group.add(cb)
        rect_xx += 23
        
    for p in range(5):        
        tmp_rect_x = 0
        for l in range (p+1):
            cb = Cracked_Brick()
            cb.rect.x = tmp_rect_x
            cb.rect.y = tmp_rect_y
            cracked_brick_group.add(cb)
            tmp_rect_x += 23
        tmp_rect_y += 23
    cb = Cracked_Brick()
    cb.rect.x = 23*8
    cb.rect.y = 23*12
    cracked_brick_group.add(cb)
    
    pygame.init()
    
    #####################################
    
    # 처음 게임 상태
    game_state = GAME_INIT
    size = (400, 361)
    screen = pygame.display.set_mode(size)
          
    run = True
    clock = pygame.time.Clock()

    while run:
        # 1) 사용자 입력 처리
        if Mario.rect.x <= 0:
            #print('reset')
            Mario.rect.x += 10
        if Mario.rect.x >= 400:
            #print('reset')
            Mario.rect.x -= 10
        keys = pygame.key.get_pressed()
        Mario.rect.centerx = (Mario.rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel)
        
        
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if game_state == GAME_INIT:
                        game_state = GAME_STAGE1
                        Mario.rect.x = 100
                        background_img = background_img_game
                        screen = pygame.display.set_mode(size)
            if event.type == pygame.KEYDOWN: 
                if not jump and event.key == pygame.K_SPACE:
                    jump = True
                    jumpCount = jumpMax
 
        if jump:
            #print(jumpCount, jumpMax)
            Mario.rect.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1
            #else:
            #    jump = False 

        # 2) 게임 상태 업데이트
        Mario_group.update()
        Pipe_group.update()
        
        if (game_state == GAME_STAGE1):

            ###################################################################################################
            # 충돌
        
            collided = pygame.sprite.groupcollide(Mario_group, cracked_brick_group, False, False)
            
            if collided: #충돌
                jump = 0
                jumpCount=-1
               
            else:
                if not jump:
                    Mario.rect.y-= jumpCount
                    jumpCount-=1

            ###################################################################################################

        # 3) 게임 상태 그리기

        screen.blit(Pipe.image, Pipe.rect())
        screen.blit(background_img, screen.get_rect())
        screen.blit(Mario.image, Mario.rect)
        
        if (game_state >= 2): # 게임이 시작된 경우
            for cb in cracked_brick_group.sprites():
                screen.blit(cb.image, cb.rect)

        collided_q1 += 1
        changeMario += 1
        collided_block += 1

        
        pygame.display.flip()

        clock.tick(FPS)

pygame.quit()
