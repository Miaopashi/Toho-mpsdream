import pygame
from pygame.sprite import Group
import os

import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from player import Player
from button import Button

from picture import Picture_before_all
from picture import Picture_before_game
from text import Text_before_game
from picture import Picture_before_boss1
from text import Text_before_boss1
from picture import Picture_after_boss1
from text import Text_after_boss1
from picture import Picture_before_boss2
from text import Text_before_boss2
from picture import Picture_after_boss2
from text import Text_after_boss2
from picture import Picture_before_boss3
from text import Text_before_boss3
from picture import Picture_after_boss3
from text import Text_after_boss3
from picture import Picture_after_game
from text import Text_after_game
from picture import Picture_end_game


def main():
    """运行整个游戏"""
    # 初始化游戏设置和窗口
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 70)
    pygame.display.set_caption('东方阿猫梦')
    pygame.mixer.init()

    # 引入基本变量
    # 载入最高分
    with open('high_score.txt', 'r') as hs:
        high_score = hs.read()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings, high_score)
    sb = Scoreboard(ai_settings, screen, stats)

    continue_button = Button(ai_settings, screen, 'to be continue...')
    reimu = Player(ai_settings, screen)
    my_bullets = Group()

    p_ba = Picture_before_all(screen)
    p_b0 = Picture_before_game(screen)
    t_b0 = Text_before_game(screen)
    p_b1 = Picture_before_boss1(ai_settings, screen)
    t_b1 = Text_before_boss1(screen)
    p_a1 = Picture_after_boss1(ai_settings, screen)
    t_a1 = Text_after_boss1(screen)
    p_b2 = Picture_before_boss2(ai_settings, screen)
    t_b2 = Text_before_boss2(screen)
    p_a2 = Picture_after_boss2(ai_settings, screen)
    t_a2 = Text_after_boss2(screen)
    p_b3 = Picture_before_boss3(ai_settings, screen)
    t_b3 = Text_before_boss3(screen)
    p_a3 = Picture_after_boss3(ai_settings, screen)
    t_a3 = Text_after_boss3(screen)
    p_a0 = Picture_after_game(screen)
    t_a0 = Text_after_game(screen)
    p_00 = Picture_end_game(ai_settings, screen)

    # 运行游戏
    gf.before_all(ai_settings, p_ba)
    gf.before_game(ai_settings, screen, t_b0, p_b0)
    pygame.mixer.music.stop()

    gf.run_game_1_first(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)
    pygame.mixer.music.stop()

    gf.before_boss1(ai_settings, screen, t_b1, p_b1)

    ai_settings.next_game = False
    gf.run_game_1_second(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)
    pygame.mixer.music.stop()

    gf.after_boss1(ai_settings, screen, t_a1, p_a1)

    ai_settings.next_game = False
    gf.run_game_2_first(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)
    pygame.mixer.music.stop()

    gf.before_boss2(ai_settings, screen, t_b2, p_b2)

    ai_settings.next_game = False
    gf.run_game_2_second(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)
    pygame.mixer.music.stop()

    gf.after_boss2(ai_settings, screen, t_a2, p_a2)

    ai_settings.next_game = False
    gf.run_game_3_first(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)
    pygame.mixer.music.stop()

    gf.before_boss3(ai_settings, screen, t_b3, p_b3)

    ai_settings.next_game = False
    gf.run_game_3_second(ai_settings, screen, stats, sb, reimu, my_bullets, continue_button)

    gf.after_boss3(ai_settings, screen, t_a3, p_a3)
    pygame.mixer.music.stop()

    gf.after_game(ai_settings, screen, t_a0, p_a0)
    pygame.mixer.music.stop()

    gf.end_game(ai_settings, screen, p_00, stats)
    pygame.mixer.music.stop()


if __name__ == '__main__':
    main()