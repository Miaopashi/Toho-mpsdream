import pygame.font
from pygame.sprite import Group
from player import Player

class Scoreboard():
    '''显示得分的类'''
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #得分字体设置
        self.text_color = 0, 0, 0
        self.font = pygame.font.SysFont('arial', 48)
        self.text_color_2 = 250, 5, 89

        self.prep_score()
        self.prep_reimus()
        self.prep_continue()

    def prep_score(self):
        '''将得分转换成渲染图像'''
        score_num = self.stats.score 
        score_str = '{:,}'.format(score_num)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.ai_settings.screen_width - 20
        self.score_rect.top = 5 + self.score_rect.height


    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.reimus.draw(self.screen)

    
    def prep_continue(self):
        times_str = 'Reborn:{:,}'.format(self.stats.continue_times)
        self.times_image = self.font.render(times_str, True, self.text_color_2)

        self.times_rect = self.times_image.get_rect()
        self.times_rect.left = 0
        self.times_rect.top = 64


    def prep_high_score(self):
        '''将最高分转换成渲染图像'''
        high_score_num = self.stats.high_score
        high_score_str = '{:,}'.format(high_score_num)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.ai_settings.screen_width - 20
        self.high_score_rect.top = 5

    def show_high_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.times_image, self.times_rect)


    def prep_reimus(self):
        self.reimus = Group()
        for reimu_number in range(self.stats.life_left):
            reimu = Player(self.ai_settings, self.screen)
            reimu.rect.x = reimu_number * reimu.rect.width
            reimu.rect.y = 0
            self.reimus.add(reimu)




class HeathPoint():
    '''表示boss血条'''
    def __init__(self, ai_settings, screen, boss):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.boss = boss

        self.height = 12
        self.full_hp = self.boss.boss_hp
        self.hp_color = 223, 223, 223

        self.prep_hp()

    def prep_hp(self):
        '''更新hp'''
        self.width = (self.boss.boss_hp / self.full_hp * 
            self.ai_settings.screen_width)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = 0
        self.rect.bottom = self.ai_settings.screen_height

    def show_hp(self):
        pygame.draw.rect(self.screen, self.hp_color, self.rect)
        
