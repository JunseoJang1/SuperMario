import pygame

from pygame import draw
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

from Mario import Player
from question_mark import Question
from cracked_brick import Cracked_Brick
from Hill import Hill
from const import *

q_list = ['platform-q.png', 'platform-q1.png', 'platform-q2.png', 'platform-q3.png']
s_list = ['mario1', 'mario2', 'mario3', 'mario4', 'mario5']

FPS = 60

size = (400, 361)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Mario Bros. 1")
 
background_img_menu = pygame.image.load("Background\Mario_menu.png")
background_img_game = pygame.image.load("Background\Mario_sky.png")
background_img = background_img_menu

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
############ class ##############
        
#################################

cracked_brick_group = pygame.sprite.Group()
cracked_brick_group2 = pygame.sprite.Group()

def isonblock(meg, otherg, me, other):
    collided = pygame.sprite.groupcollide(
        meg, otherg, False, False)

    if collided:
        forcheckt = me.rect.top - 0.1
        forcheckb = me.rect.bottom + 0.1
        forcheckr = me.rect.right - 0.1
        print(other.rect.right)
        print(me.rect.y)
        print(forcheckr)
        if other.rect.bottom >= forcheckt:
            pass
        elif other.rect.top <= forcheckb:
            pass
        elif other.rect.right == me.rect.x:
            print('못가게 막아야함')
        return True
    else:
        return False

if __name__ == "__main__":

    ############# 그룹 설정 #############
    
    Mario = Player()
    Mario.rect.x = -500
    Mario.rect.y = 295
    Mario_group = pygame.sprite.Group()
    Mario_group.add(Mario)
    
    qb = Question()
    qb.rect.x = 200
    qb.rect.y = 242
    question_block_group = pygame.sprite.Group()
    question_block_group.add(qb)

    tmp_rect_y = 208
    tmp_rect_x = 0
    
    for p in range(5):        
        tmp_rect_x = 0
        for l in range (p+1):
            cb242 = Cracked_Brick()
            cb242.rect.x = tmp_rect_x
            cb242.rect.y = tmp_rect_y
            cracked_brick_group.add(cb242)
            tmp_rect_x += 23
        tmp_rect_y += 23
        
    
    for i in range (10):
        cb = Cracked_Brick()
        cb.rect.x = rect_x
        cb.rect.y = 323
        cracked_brick_group.add(cb)
        rect_x += 23
        

    for k in range (20):
        cb1 = Cracked_Brick()
        cb1.rect.x = rect_xx
        cb1.rect.y = 345
        cracked_brick_group.add(cb1)

        rect_xx += 23

                
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if game_state >= 2: # 게임 진행 상태
                if Mario.rect.x != 0: # 마리오가 끝에 있지 않다면
                    if Mario_dash == 1: # 마리오 달리기가 활성화 상태라면
                        Mario.rect.x += 3 # 더 빠르게 달리기
                    elif Mario_dash == 0: # 아님 말고
                        Mario.rect.x += 2

                else:
                    Mario.rect.x += 2
                    
        if keys[pygame.K_LEFT]:
            if game_state >= 2: # 게임 진행 상태
                if Mario.rect.x != 0: # 마리오가 끝에 있지 않다면
                    if Mario_dash == 1: # 마리오 달리기가 활성화 상태라면
                        Mario.rect.x -= 2.8 # 더 빠르게 달리기
                    elif Mario_dash == 0: # 아님 말고
                        Mario.rect.x -= 2
                else:
                    Mario.rect.x += 2

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

                if event.key == pygame.K_LSHIFT:
                    Mario.v = 5.5
                    Mario_dash = 0
                    
                if event.key == pygame.K_SPACE:
                    if Mario.isJump == 0:
                        Mario.jump(1)
                    elif Mario.isJump == 1:
                        Mario.jump(2)
                    elif Mario.isJump == 2:
                        Mario.jump(3)

                    if Mario.isJump > 3:
                        Mario.jump(0)
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    Mario.v = 7
                    Mario_dash = 1
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(pygame.mouse.get_pos())

        #
        #
        #

        # 2) 게임 상태 업데이트
        Mario_group.update()
        question_block_group.update()
        
        if (game_state == GAME_STAGE1):

            ###################################################################################################
            
            # 충돌
            def forrr(ta):
                for ta in cracked_brick_group.sprites():
                    return ta
            if isonblock(Mario_group, cracked_brick_group, Mario, forrr(cb)) == True:
                pass
            else:
                print('실패')
                Mario.rect.y += 5
            """
            if Mario.standing() or Mario.standing(cracked_brick_group2):

                    if cb.rect.y == Mario.rect.y:
                        print('어라ㅏㅏㅏㅏ라?')
                        Mario.rect.x -= 23
            else:
                print('떨어진다ㅏㅏ')
                Mario.rect.y += 5
                """
            
                    
            ###################################################################################################
                
            
        # 물음표 블럭과 부딫친 경우
        collided_question = pygame.sprite.groupcollide(
            Mario_group, question_block_group, False, False)

        if collided_question:
            collided_qq = 1
            qb.image_change("Blocks\platform-air.png")

        #
        #
        #

        # 3) 게임 상태 그리기
        screen.blit(background_img, screen.get_rect())
        screen.blit(Mario.image, Mario.rect)
        
        if (game_state >= 2): # 게임이 시작된 경우
            for cb in cracked_brick_group.sprites():
                screen.blit(cb.image, cb.rect)
            for cb1 in cracked_brick_group.sprites():
                screen.blit(cb1.image, cb1.rect)
            for cb2 in cracked_brick_group2.sprites():
                screen.blit(cb2.image, cb2.rect)

        if collided_qq != 1:
            if (collided_q1 % 23) < 4:
                change_color = ('Blocks\\' + q_list[collided_q1 % 4])
                qb.image_change(change_color)
                question_block_group.update()
                                   

        collided_q1 += 1
        changeMario += 1
        collided_block += 1

        
        pygame.display.flip()

        clock.tick(FPS)

pygame.quit()
