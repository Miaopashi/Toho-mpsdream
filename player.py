import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    '''用来表示自机（灵梦）的类'''

    def __init__(self, ai_settings, screen):
        '''初始化自机，设置初始位置'''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        #加载灵梦的图像，获得其矩形
        self.image = pygame.image.load('images/Reimu.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将灵梦放到顶部附近
        self.rect.centerx = 30
        self.rect.centery = self.ai_settings.screen_height / 2

        #将灵梦的位置属性存储成小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #攻击标志
        self.shooting = False

    
    def update(self):
        '''根据标志移动自机'''
        if self.moving_right and self.centerx <= self.screen_rect.right:
            self.centerx += self.ai_settings.my_speed_factor
        if self.moving_left and self.centerx >= 0:
            self.centerx -= self.ai_settings.my_speed_factor
        if self.moving_up and self.centery >= self.screen_rect.top:
            self.centery -= self.ai_settings.my_speed_factor
        if self.moving_down and self.centery <= self.screen_rect.bottom:
            self.centery += self.ai_settings.my_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        '''绘制自机'''
        self.screen.blit(self.image, self.rect)


    def relive(self):
        '''再生自机'''
        self.centerx = 30
        self.centery = self.ai_settings.screen_height / 2

    def stop(self):
        '''让灵梦停下来'''
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False

