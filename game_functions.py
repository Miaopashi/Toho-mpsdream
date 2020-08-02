import sys
from time import sleep
import time
from random import random

import pygame
from pygame.sprite import Group

from bullet import My_bullet_1
from bullet import Bullet_s1
from bullet import Bullet_b1
from sprite import Sprite_1
from boss import Daiyousei
from bullet import Bullet_s2
from sprite import Sprite_2
from boss import Cirno
from bullet import Bullet_b2
from sprite import Sprite_3
from bullet import Bullet_s3
from boss import Seiga
from bullet import Bullet_b3
from bullet import Bullet_b4

from scoreboard import HeathPoint


#引入音效
pygame.mixer.init()
sound_1 = pygame.mixer.Sound('music/enep00.wav')
sound_2 = pygame.mixer.Sound('music/enep02.wav')
sound_3 = pygame.mixer.Sound('music/enep01.wav')
sound_0 = pygame.mixer.Sound('music/combobreak.mp3')
bgm_11 = 'music/bgm_11.mp3'
bgm_12 = 'music/bgm_12.mp3'
bgm_21 = 'music/bgm_21.mp3'
bgm_22 = 'music/bgm_22.mp3'
bgm_31 = 'music/bgm_31.mp3'
bgm_32 = 'music/bgm_32.mp3'
bgm_ba = 'music/bgm_ba.mp3'
bgm_aa = 'music/bgm_aa.mp3'
bgm_00 = 'music/bgm_00.mp3'


def run_game_1_first(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''运行第一面开头'''
    pygame.mixer.music.load(bgm_11)
    pygame.mixer.music.play(-1, 0)
    #创建第一面的对象
    sprites_1 = Group()
    bullets_s1 = Group()
    boss_1 = Daiyousei(ai_settings, screen)#用来凑数的

    create_fleet(ai_settings, screen, sprites_1, ai_settings.sprite_1_num, 1)

    #游戏循环
    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active and  not ai_settings.next_game:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_1, boss_1, 
                my_bullets, ai_settings.sprite_1_num, 1)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_s1)
            update_sprites(ai_settings, screen, sprites_1, boss_1, my_bullets, 
                bullets_s1, 1)

        update_screen(ai_settings, screen, sb, reimu, sprites_1, my_bullets, 
            bullets_s1, ai_settings.game_1_bg_image, continue_button)


def run_game_1_second(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''运行第一面的boss关'''
    pygame.mixer.music.load(bgm_12)
    pygame.mixer.music.play(-1, 0)
    #创建第一面boss关的对象
    boss_1 = Daiyousei(ai_settings, screen)
    bullets_b1 = Group()
    sprites_1 = Group() #也是用来凑数的

    hp = HeathPoint(ai_settings, screen, boss_1)

    #调整属性值
    ai_settings.enemy_direction = 1
    #防止灵梦乱动
    reimu.stop()

    #游戏循环
    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active and  not ai_settings.next_game:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_1, boss_1, 
                my_bullets, ai_settings.sprite_1_num, -1)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_b1)
            update_boss(ai_settings, screen, sprites_1, boss_1, my_bullets, 
                bullets_b1, -1)

        update_screen_boss(ai_settings, screen, sb, reimu, boss_1, my_bullets, 
            bullets_b1, ai_settings.game_1_bg_image, continue_button, hp)


def run_game_2_first(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''运行第二面的道中'''
    pygame.mixer.music.load(bgm_21)
    pygame.mixer.music.play(-1, 0)
    #创建要用到的变量
    sprites_2 = Group()
    bullets_s2 = Group()
    boss_2 = Cirno(ai_settings, screen) #用来凑数的

    #防止灵梦乱动
    reimu.stop()

    create_fleet(ai_settings, screen, sprites_2, ai_settings.sprite_2_num, 2)

    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_2, boss_2, 
                my_bullets, ai_settings.sprite_2_num, 2)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_s2)
            update_sprites(ai_settings, screen, sprites_2, boss_2, my_bullets, 
                bullets_s2, 2)
            
        update_screen(ai_settings, screen, sb, reimu, sprites_2, my_bullets, 
            bullets_s2, ai_settings.game_2_bg_image, continue_button)


def run_game_2_second(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''运行第二面boss'''
    pygame.mixer.music.load(bgm_22)
    pygame.mixer.music.play(-1, 0)
    #创建变量
    sprites_2 = Group()
    boss_2 = Cirno(ai_settings, screen)
    bullets_b2 = Group()

    hp = HeathPoint(ai_settings, screen, boss_2)

    #防止灵梦乱动
    reimu.stop()

    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_2, boss_2, 
                my_bullets, ai_settings.sprite_2_num, -2)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_b2)
            update_boss(ai_settings, screen, sprites_2, boss_2, my_bullets, 
                bullets_b2, -2)

        update_screen_boss(ai_settings, screen, sb, reimu, boss_2, my_bullets, 
            bullets_b2, ai_settings.game_2_bg_image, continue_button, hp)


def run_game_3_first(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''开始运行游戏第三面'''
    pygame.mixer.music.load(bgm_31)
    pygame.mixer.music.play(-1, 0)
    #创建变量
    sprites_3 = Group()
    bullets_s3 = Group()
    boss_3 = Seiga(ai_settings, screen) #用来凑数的

    #防止灵梦乱动
    reimu.stop()

    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_3, boss_3, 
                my_bullets, ai_settings.sprite_3_num, 3)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_s3)
            update_sprites(ai_settings, screen, sprites_3, boss_3, 
                my_bullets, bullets_s3, 3)

        update_screen(ai_settings, screen, sb, reimu, sprites_3, my_bullets, 
            bullets_s3, ai_settings.game_3_bg_image, continue_button)


def run_game_3_second(ai_settings, screen, stats, sb, reimu, my_bullets, 
        continue_button):
    '''运行最后的boss关'''
    pygame.mixer.music.load(bgm_32)
    pygame.mixer.music.play(-1, 0)
    #引入变量
    sprites_3 = Group()#凑数用的
    bullets_b3 = Group()
    boss_3 = Seiga(ai_settings, screen)

    hp = HeathPoint(ai_settings, screen, boss_3)

    #防止灵梦乱动
    reimu.stop()

    while not ai_settings.next_game:
        check_events(ai_settings, screen, stats, sb, reimu, my_bullets, 
            continue_button)

        if ai_settings.game_active:
            reimu.update()
            update_bullet(ai_settings, screen, stats, sprites_3, boss_3, 
                my_bullets, ai_settings.sprite_3_num, -3)
            update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
                bullets_b3)
            update_boss(ai_settings, screen, sprites_3, boss_3, my_bullets, 
                bullets_b3, -3)

        update_screen_boss(ai_settings, screen, sb, reimu, boss_3, my_bullets, 
            bullets_b3, ai_settings.game_3_bg_image, continue_button, hp)

    if stats.life_left == 3:
        stats.score += 1000


def update_screen(ai_settings, screen, sb, reimu, sprites, my_bullets, 
        enemy_bullets, bg_image, continue_button):
    '''更新屏幕'''
    screen.fill(ai_settings.bg_color)
    screen.blit(bg_image, screen.get_rect())

    for bullet in my_bullets.sprites():
        bullet.draw_bullet()
    reimu.blitme()
    sprites.draw(screen)
    for bullet in enemy_bullets.sprites():
        bullet.draw_bullet()

    sb.prep_continue()
    sb.prep_score()
    check_high_score(sb.stats, sb)
    sb.prep_high_score()
    sb.prep_reimus()

    sb.show_score()
    sb.show_high_score()

    if not ai_settings.game_active:
        continue_button.draw_button()
    
    pygame.display.flip()


def update_screen_boss(ai_settings, screen, sb, reimu, boss, my_bullets, 
        enemy_bullets, bg_image, continue_button, hp):
    '''更新屏幕'''

    screen.fill(ai_settings.bg_color)
    screen.blit(bg_image, screen.get_rect())

    for bullet in my_bullets.sprites():
        bullet.draw_bullet()
    reimu.blitme()
    boss.blit_boss()
    for bullet in enemy_bullets.sprites():
        bullet.draw_bullet()

    sb.prep_continue()    
    sb.prep_score()
    check_high_score(sb.stats, sb)
    sb.prep_high_score()
    sb.prep_reimus()

    sb.show_score()
    sb.show_high_score()

    hp.prep_hp()
    hp.show_hp()

    if not ai_settings.game_active:
        continue_button.draw_button()

    pygame.display.flip()

def update_bullet(ai_settings, screen, stats, sprites, boss, bullets, 
        number, sprite_type):
    '''当sprite_type为负数时表示boss'''
    bullets.update()

    #删除屏幕右边的自己子弹
    for bullet in bullets.copy():
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.remove(bullet)

    #响应子弹与敌机的碰撞
    if sprite_type == 1:
        #根据情况再生成小妖精
        check_bullet_sprite_collisions(ai_settings, stats, bullets, sprites)
        
        if len(sprites) == 0:
            if stats.fleet_1_left > 0:
                stats.fleet_1_left -= 1
                create_fleet(ai_settings, screen, sprites, number, 
                    sprite_type)

            elif stats.fleet_1_left == 0:
                ai_settings.next_game = True

    if sprite_type == 2:
        check_bullet_sprite_collisions(ai_settings, stats, bullets, sprites)

        if len(sprites) == 0:
            if stats.fleet_2_left > 0:
                stats.fleet_2_left -= 1
                create_fleet(ai_settings ,screen, sprites, number, 
                    sprite_type)

        elif stats.fleet_2_left == 0:
            ai_settings.next_game = True

    if sprite_type == 3:
        check_bullet_sprite_collisions(ai_settings, stats, bullets, sprites)

        if len(sprites) == 0:
            if stats.fleet_3_left > 0:
                stats.fleet_3_left -= 1
                create_fleet(ai_settings ,screen, sprites, number, 
                    sprite_type)

        elif stats.fleet_3_left == 0:
            ai_settings.next_game = True

    if sprite_type < 0 :
        check_bullet_boss_collisions(ai_settings, stats, bullets, boss)

def update_enemy_bullet(ai_settings, stats, sb, reimu, my_bullets, 
        bullets_enemy):
    '''更新敌机的子弹'''
    bullets_enemy.update()

    for bullet in bullets_enemy.copy():
        if bullet.rect.left <= 0:
            bullets_enemy.remove(bullet)

    check_reimu_bullet_collisions(ai_settings, stats, sb, reimu, 
        my_bullets, bullets_enemy)
        

def check_continue_button(ai_settings, stats, sb, reimu, continue_button, 
        mouse_x, mouse_y):
    '''玩家按下按钮的时候继续游戏'''
    button_clicked = continue_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not ai_settings.game_active:
        stats.life_left += 3
        stats.continue_times += 1
        sb.prep_continue()
        stats.score -= stats.continue_times * 100000
        sb.prep_score
        ai_settings.game_active = True
        reimu.stop()


def check_high_score(stats, sb):
    '''检查是否出现最高分'''
    if stats.score >= stats.high_score - stats.continue_times * 100000:
        stats.high_score = stats.score


def check_events(ai_settings, screen, stats, sb, reimu, bullets, continue_button):
    '''检测鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #保存最高分
            with open('high_score.txt', 'w') as hs:
                high_score = str(int(stats.high_score))
                hs.write(high_score)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, reimu, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, reimu)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_continue_button(ai_settings, stats, sb, reimu, 
                continue_button, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, screen, reimu, bullets):
    '''处理按下键的操作'''
    if event.key == pygame.K_RIGHT:
        reimu.moving_right = True
    elif event.key == pygame.K_LEFT:
        reimu.moving_left = True
    elif event.key == pygame.K_UP:
        reimu.moving_up = True
    elif event.key == pygame.K_DOWN:
        reimu.moving_down = True
    elif event.key == pygame.K_q:
        #保存最高分
        with open('high_score.txt', 'w') as hs:
                high_score = str(int(stats.high_score))
                hs.write(high_score)
        sys.exit()
    elif event.key == pygame.K_z:
        fire_bullet(ai_settings, screen, reimu, bullets)


def fire_bullet(ai_settings, screen, reimu, bullets):
    #创建一个新子弹，加入到子弹编组中
    if len(bullets) < ai_settings.my_bullets_1_allowed:
        new_bullet = My_bullet_1(ai_settings, screen, reimu)
        bullets.add(new_bullet)


def fire_barrage(ai_settings, screen, sprites, boss, bullets, sprite_type):
    '''发射敌机弹幕'''  #sprite_type为负数的时候表示boss
    if sprite_type == 1:
        fire_sprite1_barrage(ai_settings, screen, sprites, bullets)
    elif sprite_type == -1:
        fire_boss1_barrage(ai_settings, screen, boss, bullets)
    if sprite_type == 2:
        fire_sprite2_barrage(ai_settings, screen, sprites, bullets)
    elif sprite_type == -2:
        if boss.have_card:
            fire_boss2_barrage_1(ai_settings, screen, boss, bullets)
        elif not boss.have_card:
            fire_boss2_barrage_2(ai_settings, screen, boss, bullets)
    if sprite_type == 3:
        fire_sprite3_barrage(ai_settings, screen, sprites, bullets)
    elif sprite_type == -3:
        if boss.have_card:
            fire_boss3_barrage_1(ai_settings, screen, boss, bullets)
        elif not boss.have_card:
            fire_boss3_barrage_2(ai_settings, screen, boss, bullets)


def fire_sprite1_barrage(ai_settings, screen, sprites, bullets):
    '''响应第一面小妖精发射弹幕'''
    for sprite in sprites:
        if sprite.rect.y % 50 == 0 :
            new_bullet = Bullet_s1(ai_settings, screen, sprite)
            bullets.add(new_bullet)
        else:
            continue


def fire_boss1_barrage(ai_settings, screen, boss, bullets):
    '''响应大酱发射弹幕'''
    if boss.rect.y % 80 == 0:
        for times in range(ai_settings.bullet_b1_num):
            new_bullet = Bullet_b1(ai_settings, screen, boss)
            new_bullet.rect.y += (ai_settings.bullet_b1_height * 
                (times - 1) * 2)
            bullets.add(new_bullet)
    
    if boss.rect.y % 100 == 0:
        new_bullet = Bullet_b1(ai_settings, screen, boss)
        new_bullet.rect.y = new_bullet.rect.height
        bullets.add(new_bullet)


def fire_sprite2_barrage(ai_settings, screen, sprites, bullets):
    '''响应第二面的大酱（小怪）发射弹幕'''
    for sprite in sprites:
        if sprite.rect.y % 80 == 0:
            for sprite in sprites:    
                new_bullet = Bullet_s2(ai_settings, screen, sprite)
                bullets.add(new_bullet)
        else:
            continue


def fire_boss2_barrage_1(ai_settings, screen, boss, bullets):
    '''响应第二面的琪露诺发射弹幕'''
    if boss.rect.y % 80 == 0 and boss.rect.y % 160 != 0:
        bullet = Bullet_b2(ai_settings, screen, boss)
        number = get_bullets_number(ai_settings, bullet)
        for num in range(number):
            new_bullet = Bullet_b2(ai_settings, screen, boss)
            new_bullet.rect.y = (new_bullet.rect.height + 6 * num * 
                new_bullet.rect.height)
            bullets.add(new_bullet)

    elif boss.rect.y % 160 == 0:
        bullet = Bullet_b2(ai_settings, screen, boss)
        number = get_bullets_number(ai_settings, bullet)
        for num in range(number):
            new_bullet = Bullet_b2(ai_settings, screen, boss)
            new_bullet.rect.y = (new_bullet.rect.height + 6 * num * 
                new_bullet.rect.height + 3 * new_bullet.rect.height)
            bullets.add(new_bullet)
    
def get_bullets_number(ai_settings, bullet):
    '''计算屏幕可以放多少组子弹'''
    available_space_y = ai_settings.screen_height - 3 * bullet.rect.height
    number_bullets_y = int(available_space_y / (4 * bullet.rect.height))
    return number_bullets_y


def fire_boss2_barrage_2(ai_settings, screen, boss, bullets):
    '''相应第二面boss的第二幕弹幕'''
    if boss.rect.y % 10 == 0:
        num = random()
        new_bullet = Bullet_b2(ai_settings, screen, boss)
        new_bullet.rect.y = num * ai_settings.screen_height
        bullets.add(new_bullet)     


def fire_sprite3_barrage(ai_settings, screen, sprites, bullets):
    '''响应第三面油库里的弹幕'''
    for sprite in sprites:
        if sprite.rect.y % 10 == 0:
            for num in range(ai_settings.bullet_s3_num):
                new_bullet = Bullet_s3(ai_settings, screen, sprite)
                new_bullet.x -= 2 * new_bullet.rect.width * num
                bullets.add(new_bullet)


def fire_boss3_barrage_1(ai_settings, screen, boss, bullets):
    '''响应第三面的第一轮弹幕'''
    if boss.rect.centery <= 0:
        for times in range(ai_settings.bullet_b3_num):
            new_bullet = Bullet_b3(ai_settings, screen, boss)
            new_bullet.rect.y = new_bullet.rect.height
            new_bullet.rect.y += (ai_settings.bullet_b3_height * 
                (times - 1) * 2)
            bullets.add(new_bullet)

    if boss.rect.centery >= boss.ai_settings.screen_height:
        for times in range(ai_settings.bullet_b3_num):
            new_bullet = Bullet_b3(ai_settings, screen, boss)
            new_bullet.rect.y = (ai_settings.screen_height - 
                new_bullet.rect.height)
            new_bullet.rect.y += (ai_settings.bullet_b3_height * 
                (times - 1) * -2)
            bullets.add(new_bullet)   


def fire_boss3_barrage_2(ai_settings, screen, boss, bullets):
    '''响应青娥最后的符卡'''
    if boss.rect.centery <= 0:
        for num in range(2):
            new_bullet = Bullet_b4(ai_settings, screen, boss)
            new_bullet.rect.y = 2 * num * new_bullet.rect.height
            bullets.add(new_bullet)

    elif boss.rect.centery >= boss.ai_settings.screen_height:
        for num in range(2):
            new_bullet = Bullet_b4(ai_settings, screen, boss)
            new_bullet.rect.y = (new_bullet.rect.height + 2 * num * 
                new_bullet.rect.height)
            bullets.add(new_bullet)


def check_keyup_events(event, reimu):
    '''检测键盘松开的事件'''
    if event.key == pygame.K_RIGHT:
        reimu.moving_right = False
    elif event.key == pygame.K_LEFT:
        reimu.moving_left = False
    elif event.key == pygame.K_UP:
        reimu.moving_up = False
    elif event.key == pygame.K_DOWN:
        reimu.moving_down = False


def create_fleet(ai_settings, screen, sprites, number, sprite_type):
    for sprite_num in range(number):
        create_sprite(ai_settings, screen, sprites, sprite_num, sprite_type)


def create_sprite(ai_settings, screen, sprites, sprite_num, sprite_type):
    '''根据参数判断创建第几面的妖精'''
    if sprite_type == 1:
        new_sprite = Sprite_1(ai_settings, screen)
    elif sprite_type == 2:
        new_sprite = Sprite_2(ai_settings, screen)
    elif sprite_type == 3:
        new_sprite = Sprite_3(ai_settings,screen)     
    new_sprite_height = new_sprite.rect.height
    new_sprite.y = new_sprite_height * sprite_num * 2 + 10
    new_sprite.rect.y = new_sprite.y
    sprites.add(new_sprite)


def update_sprites(ai_settings, screen, sprites, boss, bullets, 
        bullets_enemy, sprite_type):
    '''在屏幕内移动小妖精并发射弹幕'''
    check_sprite_edges(ai_settings, sprites)
    sprites.update()
    fire_barrage(ai_settings, screen, sprites, boss, bullets_enemy, 
        sprite_type)
    check_fleet_bottom(ai_settings, screen, sprites)
            

def check_sprite_edges(ai_settings, sprites):
    for sprite in sprites.sprites():
        if sprite.check_edges():
            change_fleet_direction(ai_settings, sprites)
            break


def change_fleet_direction(ai_settings, sprites):
    for sprite in sprites.sprites():
        sprite.rect.x -= ai_settings.fleet_move_factor
    ai_settings.enemy_direction *= -1


def check_fleet_bottom(ai_settings, screen, sprites):
    '''检测小妖精是否到达屏幕左端'''
    screen_rect = screen.get_rect()
    for sprite in sprites.sprites():
        if sprite.rect.x <= 0:
            sprites.remove(sprite)


def check_bullet_sprite_collisions(ai_settings, stats, bullets, sprites):
    '''响应自机子弹和不同关的小妖精的碰撞'''
    global sound_1

    for sprite in sprites.copy():
        for bullet in bullets.copy():
            if (pygame.Rect.colliderect(bullet.rect, sprite.rect) and 
            sprite.sprite_hp > 0):
                bullet.remove(bullets)
                sprite.sprite_hp -= 1
        
            if sprite.sprite_hp == 0:
                stats.score += sprite.sprite_point
                sound_1.play()
                sprites.remove(sprite)
                break


def check_bullet_boss_collisions(ai_settings, stats, bullets, boss):
    '''响应自机子弹和boss的碰撞'''
    global sound_2, sound_3
    for bullet in bullets.copy():
        if (pygame.Rect.colliderect(bullet.rect, boss.rect) and 
                boss.boss_hp > 0):
            bullets.remove(bullet)
            boss.boss_hp -= 1
        if boss.boss_hp == 0 and boss.have_card:
            boss.boss_hp = ai_settings.boss_card_hp
            boss.have_card = False
            sound_2.play()
            time.sleep(0.5)
            boss.next_card()
        if boss.boss_hp == 0 and not boss.have_card:
            time.sleep(0.5)
            sound_3.play()
            stats.score += ai_settings.boss_point
            ai_settings.next_game = True
            break


def update_boss(ai_settings, screen, sprites, boss, bullets, bullets_enemy, 
        sprite_type):
    '''在屏幕内移动boss并发射弹幕'''
    check_boss_edges(ai_settings, boss)
    boss.update()
    fire_barrage(ai_settings, screen, sprites, boss, bullets_enemy, sprite_type)


def check_boss_edges(ai_settings, boss):
    '''响应boss碰到屏幕边界'''
    if boss.check_edges():
        ai_settings.enemy_direction *= -1


def check_reimu_bullet_collisions(ai_settings, stats, sb, reimu, my_bullets, 
        bullets_enemy):
    '''响应灵梦与敌机子弹的碰撞'''
    if pygame.sprite.spritecollideany(reimu, bullets_enemy):
        reimu_hit(ai_settings, stats, sb, reimu, my_bullets, bullets_enemy)


def reimu_hit(ai_settings, stats, sb, reimu, my_bullets, bullets_enemy):
    '''响应灵梦被击落'''
    global sound_0

    if stats.life_left > 0:
        bullets_enemy.empty()
        my_bullets.empty()

        stats.life_left -= 1
        sb.prep_reimus()

        sound_0.play()

        time.sleep(0.5)
    #复活回数用完的时候结束游戏
    elif stats.life_left == 0:
        ai_settings.game_active = False



#下面的函数是剧情担当
def check_read_events(ai_settings):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not ai_settings.next_page:
                    ai_settings.next_page = True
                elif ai_settings.next_page:
                    ai_settings.next_page = False
        if event.type == pygame.QUIT:
            #保存最高分
            sys.exit()


def before_all(ai_settings, p_ba):
    '''播放前言'''
    while ai_settings.next_page:
        check_read_events(ai_settings)
        p_ba.screen.fill((0, 0, 0))
        p_ba.blit_p()
        pygame.display.flip()
        pygame.time.delay(100*3)


def before_game(ai_settings, screen, t_b0, p_b0):
    '''前情摘要'''
    pygame.mixer.music.load(bgm_ba)
    pygame.mixer.music.play(-1, 0)

    ai_settings.next_page = True
    while ai_settings.next_page:
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_1, p_b0.rect_1)
        t_b0.show_text(t_b0.str_1)
        pygame.display.flip()
        pygame.time.delay(100)
        check_read_events(ai_settings)
        

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_2, p_b0.rect_2)
        t_b0.show_text(t_b0.str_2)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_3, p_b0.rect_3)
        t_b0.show_text(t_b0.str_3)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_4, p_b0.rect_4)
        t_b0.show_text(t_b0.str_4)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_5, p_b0.rect_5)
        t_b0.show_text(t_b0.str_5)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_6, p_b0.rect_6)
        t_b0.show_text(t_b0.str_6)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b0.blit_p(p_b0.image_7, p_b0.rect_7)
        t_b0.show_text(t_b0.str_7)
        pygame.display.flip()
        pygame.time.delay(100)


def before_boss1(ai_settings, screen, t_b1, p_b1):
    '''第一面中'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0)) 
        p_b1.blit_p()
        t_b1.show_text(t_b1.str_1)
        pygame.display.flip()
        pygame.time.delay(100)


def after_boss1(ai_settings, screen, t_a1, p_a1):
    '''第一面后'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a1.blit_p()
        t_a1.show_text(t_a1.str_1)
        pygame.display.flip()
        pygame.time.delay(100)

    
def before_boss2(ai_settings, screen, t_b2, p_b2):
    '''第二面中'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_b2.blit_p()
        t_b2.show_text(t_b2.str_1)
        pygame.display.flip()
        pygame.time.delay(100)


def after_boss2(ai_settings, screen, t_a2, p_a2):
    '''第二面后'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))     
        p_a2.blit_p()
        t_a2.show_text(t_a2.str_1)
        pygame.display.flip()
        pygame.time.delay(100)


def before_boss3(ai_settings, screen, t_b3, p_b3):
    '''第二面中'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0)) 
        p_b3.blit_p()
        t_b3.show_text(t_b3.str_1)
        pygame.display.flip()
        pygame.time.delay(100)


def after_boss3(ai_settings, screen, t_a3, p_a3):
    '''第二面后'''
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a3.blit_p()
        t_a3.show_text(t_a3.str_1)
        pygame.display.flip()
        pygame.time.delay(100)


def after_game(ai_settings, screen, t_a0, p_a0):
    '''日后谈'''
    pygame.mixer.music.load(bgm_aa)
    pygame.mixer.music.play(-1, 0)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a0.blit_p(p_a0.image_1, p_a0.rect_1)
        t_a0.show_text(t_a0.str_1)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a0.blit_p(p_a0.image_2, p_a0.rect_2)
        t_a0.show_text(t_a0.str_2)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a0.blit_p(p_a0.image_3, p_a0.rect_3)
        t_a0.show_text(t_a0.str_3)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a0.blit_p(p_a0.image_4, p_a0.rect_4)
        t_a0.show_text(t_a0.str_4)
        pygame.display.flip()
        pygame.time.delay(100)

    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        screen.fill((0, 0, 0))
        p_a0.blit_p(p_a0.image_5, p_a0.rect_5)
        t_a0.show_text(t_a0.str_5)
        pygame.display.flip()
        pygame.time.delay(100)


def end_game(ai_settings, screen, p_00, stats):
    '''写在最后'''
    pygame.mixer.music.load(bgm_00)
    pygame.mixer.music.play(1, 0)
    
    screen.fill((0, 0, 0))

    #保存最高分
    with open('high_score.txt', 'w') as hs:
                high_score = str(int(stats.high_score))
                hs.write(high_score)
                
    ai_settings.next_page = True
    while ai_settings.next_page:
        check_read_events(ai_settings)
        if p_00.rect_1.centery > p_00.screen_rect.centery:
            p_00.update()
        p_00.blit_p()
        pygame.display.flip()
        pygame.time.delay(100)


#辛苦了