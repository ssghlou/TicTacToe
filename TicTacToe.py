# encoding:utf-8
import pygame

import function as f
from chess import Chess,BigChess
from button import Button
from settings import Settings
from windows import Windows

def run_game():
    pygame.init()   #初始化
    st = Settings()
    screen = pygame.display.set_mode(st.setmode) #500*600的屏幕
    pygame.display.set_caption('Chess')         #标题
    
    image = pygame.image.load('materials/chessboard.bmp') #载入棋盘
    chess = Chess()
    bigchess = BigChess()
    retract_button = Button(screen,'Retract',st.retract_button_position[0],
        st.retract_button_position[1])      #悔棋按钮
    replay_button = Button(screen,'Replay',st.replay_button_position[0],
        st.replay_button_position[1])      #重玩按钮
    windows = Windows(screen,'Replay?','Yes','No',150,200)
    while True:
        screen.fill(st.bg_color)      #背景色
        screen.blit(image,st.top_left_corner)#在棋盘左上角位置绘制棋盘，注意跟棋盘的中心位置有关
        
        f.check_keydown(chess,bigchess,windows,screen,st,retract_button,replay_button)#检测鼠标按动
        # f.ai(chess,bigchess,st)
        f.draw(chess,bigchess,screen,windows,st)    #绘制棋子，框等
        
        retract_button.draw_button()    #绘制悔棋按钮
        replay_button.draw_button()     #绘制重玩按钮
        pygame.display.update()     #更新屏幕
        
run_game()
