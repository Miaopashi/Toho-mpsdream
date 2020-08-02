import pygame

class Settings():
    '''存储《东方阿猫梦》中的所有设置的类'''

    def __init__(self):
        '''初始化游戏的各项设置'''
        #静态设置（后面的分数递增）
        #屏幕设置
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (60, 60, 60)

        #游戏背景
        self.game_1_bg_image = pygame.image.load('images/game_1_bg.jpg')
        self.game_2_bg_image = pygame.image.load('images/game_2_bg.jpg')
        self.game_3_bg_image = pygame.image.load('images/game_3_bg.jpg')

        #游戏开始、关卡完成和waring标志
        self.game_active = True
        self.next_game = False
        self.waring = False
        self.next_page = True

        # 敌机的设定
        self.enemy_direction = 1 
        self.fleet_speed_factor = 3
        self.fleet_move_factor = 8

        self.boss_speed_factor = 6
        self.boss_card_hp = 50
        self.boss_point = 336720
        # 一面的小妖精
        self.sprite_1_num = 3
        self.sprite_1_hp = 3
        self.sprite_1_point = 28000
        self.fleet_1_num = 3
        self.bullet_s1_color = 66, 204, 255
        self.bullet_s1_speed_factor = 2
        self.bullet_s1_width = 10
        self.bullet_s1_height = 10

        #二面的小妖精
        self.sprite_2_num = 4
        self.sprite_2_point = 28000
        self.sprite_2_hp = 3
        self.fleet_2_num = 3
        self.bullet_s2_color = 251, 250, 211
        self.bullet_s2_speed_factor = 2
        self.bullet_s2_width = 10
        self.bullet_s2_height = 10
        
        # 三面的油库里
        self.sprite_3_num = 4
        self.sprite_3_point = 20990
        self.sprite_3_hp = 8
        self.fleet_3_num = 4
        self.bullet_s3_num = 4
        self.bullet_s3_color = 250, 185, 91
        self.bullet_s3_speed_factor = 3
        self.bullet_s3_width = 30
        self.bullet_s3_height = 10
        
        # 大酱
        self.daiyousei_num = 1
        self.daiyousei_hp = 50
        self.bullet_b1_speed_factor = 3
        self.bullet_b1_width = 20
        self.bullet_b1_height = 20
        self.bullet_b1_num = 5
        self.bullet_b1_color = 251, 250, 211

        # 琪露诺
        self.cirno_num = 1
        self.cirno_hp = 50
        self.bullet_b2_speed_factor = 3
        self.bullet_b2_width = 25
        self.bullet_b2_height = 25
        self.bullet_b2_num = 3
        self.bullet_b2_color = 5, 13, 89
        # 霍青娥 和 宫古芳香
        self.seiga_hp = 50
        self.yoshika_hp = 10
        self.bullet_b3_speed_factor = 3
        self.bullet_b3_width = 50
        self.bullet_b3_height = 25
        self.bullet_b3_num = 10
        self.bullet_b3_color = 35, 163, 147
        self.bullet_b4_speed_factor = 5
        
        # 自机设定
        # 自机的子弹
        self.my_bullets_1_width = 50
        self.my_bullets_1_height = 12
        self.my_bullets_1_color = 250, 5, 89
        self.my_bullets_1_speed_factor = 15
        self.my_bullets_1_allowed = 4
        # 自机的大招（根本就没有做！）
        self.outcoming_limit = 3
        # 博丽灵梦
        self.my_speed_factor = 6
        self.my_life_limit = 3
        

        #动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的值'''
        self.sprite_1_fleet = 3
        self.sprite_2_fleet = 4
        self.yukuri_fleet = 4
        self.boss_life = 2