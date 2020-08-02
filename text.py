import pygame
import pygame.font
import codecs

'''用来表示文本的类'''
class Text_before_game():
    '''前情摘要'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/b0_1.txt'
        self.str_2 = 'text/b0_2.txt'
        self.str_3 = 'text/b0_3.txt'
        self.str_4 = 'text/b0_4.txt'
        self.str_5 = 'text/b0_5.txt'
        self.str_6 = 'text/b0_6.txt'
        self.str_7 = 'text/b0_7.txt'


    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_before_boss1():
    '''第一面中'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/b1.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_after_boss1():
    '''第一面后'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/a1.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_before_boss2():
    '''第二面中'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/b2.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_after_boss2():
    '''第二面后'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/a2.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_before_boss3():
    '''第三面前'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/b3.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_after_boss3():
    '''第三面后'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/a3.txt'

    def show_text(self, string):
        '''将得分转换成渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)


class Text_after_game():
    '''日后谈'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = 255, 255, 255
        self.text_color = 112, 69, 175
        self.font =  pygame.font.SysFont('simhei', 24)

        self.str_1 = 'text/a0_1.txt'
        self.str_2 = 'text/a0_2.txt'
        self.str_3 = 'text/a0_3.txt'
        self.str_4 = 'text/a0_4.txt'
        self.str_5 = 'text/a0_5.txt'
        self.str_6 = 'text/a0_6.txt'
        self.str_7 = 'text/a0_7.txt'


    def show_text(self, string):
        '''渲染图像'''
        number = -1
        txt = codecs.open(string, encoding='gb2312')
        for line in txt:
            text = line.rstrip()
            number += 1
            self.image = self.font.render(text, True, 
                self.text_color, self.bg_color)
            self.rect = self.image.get_rect()
            self.rect.x = 20 + number * self.rect.height
            self.rect.top = 720 - self.rect.height * (4 - number)

            self.screen.blit(self.image, self.rect)