
class GameStats():
    '''用于统计游戏数据，包括剩余残机数，剩余符卡数，游戏得分'''
    def __init__(self, ai_settings, high_score):
        '''初始化统计数据'''
        self.ai_settings = ai_settings
        self.reset_stats()

        self.high_score = int(high_score)

    def reset_stats(self):
        '''初始化游戏开始时需要重置的统计数据'''
        self.continue_times = 0
        self.score = 0
        self.life_left = self.ai_settings.my_life_limit
        self.fleet_1_left = self.ai_settings.fleet_1_num
        self.fleet_2_left = self.ai_settings.fleet_2_num
        self.fleet_3_left = self.ai_settings.fleet_3_num