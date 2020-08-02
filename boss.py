import pygame


class Daiyousei:

    def __init__(self, ai_settings, screen):
        """初始化大酱"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.y = 0
        # 是否有符卡的标志
        self.have_card = False

        self.image = pygame.image.load('images/Daiyousei_boss.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - self.rect.width
        self.rect.y = self.rect.height * 2

        self.boss_shot = 0
        self.boss_hp = self.ai_settings.daiyousei_hp

    def blit_boss(self):
        '''指定位置绘制大酱'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.y <= 0:
            return True
        elif self.rect.y >= self.ai_settings.screen_height - 200:
            return True

    def update(self):
        self.y += (self.ai_settings.boss_speed_factor *
                   self.ai_settings.enemy_direction)
        self.rect.y = self.y

    def next_card(self):
        self.ai_settings.next_game = True

    def use_card(self):
        pass


class Cirno():

    def __init__(self, ai_settings, screen):
        '''初始化琪露诺'''
        self.ai_settings = ai_settings
        self.screen = screen
        self.y = 0
        # 是否有符卡的标志
        self.have_card = True

        self.image = pygame.image.load('images/Cirno_boss_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - self.rect.width
        self.rect.y = self.rect.height

        self.boss_shot = 0
        self.boss_hp = ai_settings.cirno_hp

    def blit_boss(self):
        '''指定位置绘制琪露诺'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.centery <= 50:
            return True
        elif self.rect.y >= self.ai_settings.screen_height - 200:
            return True

    def update(self):
        self.y += (self.ai_settings.boss_speed_factor *
                   self.ai_settings.enemy_direction)
        self.rect.y = self.y

    def next_card(self):
        '''切换琪露诺的符卡'''
        self.image = pygame.image.load('images/Cirno_boss_2.png')

    def use_card(self):
        '''显示符卡'''
        self.card_image = pygame.image.load('images/Cirno_card.jpg')
        self.card_rect = self.card_image.get_rect()
        self.card_rect.center = self.screen_rect.center
        self.screen.blit(self.card_image, self.card_rect)


class Seiga():

    def __init__(self, ai_settings, screen):
        '''初始化霍青娥'''
        self.ai_settings = ai_settings
        self.screen = screen
        self.y = 0
        # 是否有符卡的标志
        self.have_card = True

        self.image = pygame.image.load('images/Seiga_boss_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.screen_rect.width - self.rect.width * 1.5
        self.rect.y = self.rect.height

        self.boss_hp = ai_settings.cirno_hp

    def blit_boss(self):
        '''指定位置绘制霍青娥'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.centery <= 0:
            return True
        elif self.rect.centery >= self.ai_settings.screen_height:
            return True

    def update(self):
        self.y += (self.ai_settings.boss_speed_factor * 1.6 *
                   self.ai_settings.enemy_direction)
        self.rect.y = self.y

    def next_card(self):
        '''切换霍青娥的符卡'''
        self.image = pygame.image.load('images/Seiga_boss_2.png')

    def use_card(self):
        '''显示符卡'''
        self.card_image = pygame.image.load('images/Seiga_card.jpg')
        self.card_rect = self.card_image.get_rect()
        self.card_rect.x = 600
        self.card_rect.y = 300
        self.screen.blit(self.card_image, self.card_rect)
