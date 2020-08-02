import pygame.font

class Button():
    '''表示游戏结束的按钮'''
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 280, 50
        self.button_color = 112, 69, 175
        self.text_color = 0, 0, 0
        self.font = pygame.font.SysFont('arial', 48)

        #创建按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #创建文本对象
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将文字转换为渲染图像'''
        self.button_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.button_image_rect = self.button_image.get_rect()
        self.button_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制按钮，绘制文字'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.button_image, self.button_image_rect)