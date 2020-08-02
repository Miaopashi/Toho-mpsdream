import pygame

'''表示剧情插图的类'''
class Picture_before_all():
    '''前言'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ba_image = pygame.image.load('images/before_all.png')
        self.rect = self.ba_image.get_rect()
        self.rect.center = self.screen_rect.center

    def blit_p(self):
        self.screen.blit(self.ba_image, self.rect)


class Picture_before_game():
    '''前情摘要'''
    def __init__(self, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()

        self.image_1 = pygame.image.load('images/b0_1.jpg')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.center = self.screen_rect.center

        self.image_2 = pygame.image.load('images/b0_2.jpg')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.center = self.screen_rect.center

        self.image_3 = pygame.image.load('images/b0_3.png')
        self.rect_3 = self.image_3.get_rect()
        self.rect_3.center = self.screen_rect.center

        self.image_4 = pygame.image.load('images/b0_4.jpg')
        self.rect_4 = self.image_4.get_rect()
        self.rect_4.center = self.screen_rect.center

        self.image_5 = pygame.image.load('images/b0_5.jpg')
        self.rect_5 = self.image_5.get_rect()
        self.rect_5.center = self.screen_rect.center

        self.image_6 = pygame.image.load('images/b0_6.jpg')
        self.rect_6 = self.image_6.get_rect()
        self.rect_6.center = self.screen_rect.center

        self.image_7 = pygame.image.load('images/b0_7.jpg')
        self.rect_7 = self.image_7.get_rect()
        self.rect_7.center = self.screen_rect.center

    def blit_p(self, image, rect):
        self.screen.blit(image, rect)



class Picture_before_boss1():
    '''第一面中'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/b1_1.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.ai_settings.screen_width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

        self.image_2 = pygame.image.load('images/reimu_p.png')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.left = 0
        self.rect_2.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_1_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)


class Picture_after_boss1():
    '''第一面后'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/reimu_p.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.rect_1.width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_1_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)


class Picture_before_boss2():
    '''第二面中'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/b2.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.ai_settings.screen_width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

        self.image_2 = pygame.image.load('images/reimu_p.png')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.left = 0
        self.rect_2.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_2_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)


class Picture_after_boss2():
    '''第二面后'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/a2.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.ai_settings.screen_width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

        self.image_2 = pygame.image.load('images/reimu_p.png')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.left = 0
        self.rect_2.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_2_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)


class Picture_before_boss3():
    '''第三面中'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/b3.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.ai_settings.screen_width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

        self.image_2 = pygame.image.load('images/reimu_p.png')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.left = 0
        self.rect_2.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_3_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)


class Picture_after_boss3():
    '''第三面后'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/a3.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.right = self.ai_settings.screen_width
        self.rect_1.bottom = ai_settings.screen_height - (20 + 24 * 4)

        self.image_2 = pygame.image.load('images/reimu_p.png')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.left = 0
        self.rect_2.bottom = ai_settings.screen_height - (20 + 24 * 4)

    def blit_p(self):
        self.screen.blit(self.ai_settings.game_3_bg_image, self.screen_rect)
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)


class Picture_after_game():
    '''日后谈'''
    def __init__(self, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()

        self.image_1 = pygame.image.load('images/a0_1.jpg')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.center = self.screen_rect.center

        self.image_2 = pygame.image.load('images/a0_2.jpg')
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.center = self.screen_rect.center

        self.image_3 = pygame.image.load('images/a0_3.jpg')
        self.rect_3 = self.image_3.get_rect()
        self.rect_3.center = self.screen_rect.center

        self.image_4 = pygame.image.load('images/a0_4.jpg')
        self.rect_4 = self.image_4.get_rect()
        self.rect_4.center = self.screen_rect.center

        self.image_5 = pygame.image.load('images/a0_5.jpg')
        self.rect_5 = self.image_5.get_rect()
        self.rect_5.center = self.screen_rect.center

    def blit_p(self, image, rect):
        self.screen.blit(image, rect)


class Picture_end_game():
    '''写在最后'''
    def __init__(self, ai_settings, screen):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.image_1 = pygame.image.load('images/00.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.centerx = self.screen_rect.centerx
        self.rect_1.y = self.ai_settings.screen_height

    def blit_p(self):
        self.screen.blit(self.image_1, self.rect_1)

    def update(self):
        self.rect_1.y -= 2