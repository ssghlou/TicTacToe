class Settings():
    def __init__(self):
        self.bg_color = (137,207,240)   #背景色
        self.setmode = (500,600)        #窗口的大小
        self.retract_button_position = (200,100)#悔棋按钮的坐标
        self.replay_button_position = (200,50)  #重玩按钮的坐标
        self.center_x = 250   #棋盘中心的x坐标
        self.center_y = 400   #棋盘中心的y坐标
        self.chessboard_width = 300     #棋盘的宽度
        self.top_left_corner = (self.center_x-self.chessboard_width//2,
            self.center_y-self.chessboard_width//2) #棋盘左上角的坐标
        self.game_active = True     #若游戏结束，一方获胜，则为False
        self.win = -1      #-1为未决出胜负，0为平局，1为X方获胜，2为O方获胜
        self.active_windows = False     #窗口是否显示
