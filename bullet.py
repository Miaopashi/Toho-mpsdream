'''建立多个对各种子弹管理的类'''

import pygame
from pygame.sprite import Sprite

class My_bullet_1(Sprite):

    def __init__(self, ai_settings, screen, reimu):
        '''初始化自机弹幕的设置'''
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.my_bullets_1_width,
            ai_settings.my_bullets_1_height)
        self.rect.left = reimu.rect.right
        self.rect.centery = reimu.rect.centery
        self.x = float(self.rect.x)

        self.color = ai_settings.my_bullets_1_color
        self.speed_factor = ai_settings.my_bullets_1_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_s1(Sprite):

    def __init__(self, ai_settings, screen, sprite):
        '''初始化小妖精（小琪露诺）弹幕的设置'''
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_s1_width,
            ai_settings.bullet_s1_height)
        self.rect.left = sprite.rect.right
        self.rect.centery = sprite.rect.centery
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_s1_color
        self.speed_factor = ai_settings.bullet_s1_speed_factor

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_b1(Sprite):
    '''创建表示大酱弹幕的类'''
    def __init__(self, ai_settings, screen, boss):    
        super().__init__()
        self.screen = screen

        self.color = ai_settings.bullet_b1_color
        self.speed_factor = ai_settings.bullet_b1_speed_factor

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_b1_width,
            ai_settings.bullet_b1_height)
        self.rect.left = boss.rect.right
        self.rect.centery = boss.rect.centery
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_s2(Sprite):

    def __init__(self, ai_settings, screen, sprite):
        '''初始化小妖精（雾）弹幕的设置'''
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_s2_width,
            ai_settings.bullet_s2_height)
        self.rect.left = sprite.rect.right
        self.rect.centery = sprite.rect.centery
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_s2_color
        self.speed_factor = ai_settings.bullet_s2_speed_factor

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_b2(Sprite):
    '''创建表示琪露诺弹幕的类'''
    def __init__(self, ai_settings, screen, boss):    
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.color = ai_settings.bullet_b2_color
        self.speed_factor = ai_settings.bullet_b2_speed_factor

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_b2_width,
            ai_settings.bullet_b2_height)
        self.rect.left = boss.rect.right
        self.rect.centery = boss.rect.centery
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_s3(Sprite):

    def __init__(self, ai_settings, screen, sprite):
        '''初始化油库里弹幕的设置'''
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_s3_width,
            ai_settings.bullet_s3_height)
        self.rect.left = sprite.rect.right
        self.rect.centery = sprite.rect.centery
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_s3_color
        self.speed_factor = ai_settings.bullet_s3_speed_factor

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_b3(Sprite):
    '''创建表示霍青娥弹幕的类'''
    def __init__(self, ai_settings, screen, boss):    
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.color = ai_settings.bullet_b3_color
        self.speed_factor = ai_settings.bullet_b3_speed_factor

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_b3_width,
            ai_settings.bullet_b3_height)
        self.rect.left = boss.rect.right
        self.rect.centery = boss.rect.centery
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_b4(Sprite):
    '''创建表示射出去的宫古芳香弹幕的类'''
    def __init__(self, ai_settings, screen, boss):    
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.speed_factor = ai_settings.bullet_b3_speed_factor

        self.image = pygame.image.load('images/Yoshika.png')
        self.rect = self.image.get_rect()

        self.rect.left = boss.rect.right
        self.rect.centery = boss.rect.centery
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
