import pygame
from pygame.sprite import Sprite

class Sprite_1(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化小妖精'''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        self.image = pygame.image.load('images/Cirno.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - 2 * self.rect.width
        self.rect.y = self.rect.height

        self.sprite_hp = self.ai_settings.sprite_1_hp
        self.sprite_point = self.ai_settings.sprite_1_point


    def check_edges(self):
        if self.rect.y <= 0:
            return True
        elif  self.rect.y >= self.ai_settings.screen_height:
            return True


    def update(self):
        '''根据方向上下移动小妖精'''
        self.y += (self.ai_settings.fleet_speed_factor * 
            self.ai_settings.enemy_direction)
        self.rect.y = self.y



class Sprite_2(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化小妖精'''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        self.image = pygame.image.load('images/Daiyousei.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - 2 * self.rect.width
        self.rect.y = self.rect.height

        self.sprite_hp = self.ai_settings.sprite_2_hp
        self.sprite_point = self.ai_settings.sprite_2_point


    def check_edges(self):
        if self.rect.y <= 0:
            return True
        elif  self.rect.y >= self.ai_settings.screen_height:
            return True


    def update(self):
        '''根据方向上下移动小妖精'''
        self.y += (self.ai_settings.fleet_speed_factor * 
            self.ai_settings.enemy_direction)
        self.rect.y = self.y



class Sprite_3(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化油库里'''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        self.image = pygame.image.load('images/Yukuri.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - 2 * self.rect.width
        self.rect.y = self.rect.height

        self.sprite_hp = self.ai_settings.sprite_3_hp
        self.sprite_point = self.ai_settings.sprite_3_point


    def check_edges(self):
        if self.rect.y <= 0:
            return True
        elif  self.rect.y >= self.ai_settings.screen_height:
            return True


    def update(self):
        '''根据方向上下移动小妖精'''
        self.y += (self.ai_settings.fleet_speed_factor * 
            self.ai_settings.enemy_direction)
        self.rect.y = self.y