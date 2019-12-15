import pygame

import function as f
from chess import Chess
from button import Button

def run_game():
    pygame.init()   #初始化
    screen = pygame.display.set_mode((500,600)) #500*600的屏幕
    pygame.display.set_caption('Chess')         #标题
    
    image = pygame.image.load('images/bg.bmp') #载入界面
    chess = Chess()
    retract_button = Button(screen,'Retract',200,100)   #悔棋按钮
    replay_button = Button(screen,'Replay',200,50)      #重玩按钮
    
    while True:
        screen.blit(image,(0,0))    #在(0,0)绘制底层图像
        
        f.check_keydown(chess,screen,retract_button,replay_button)#检测鼠标按动
        f.draw(chess,screen)    #绘制棋子，框
        
        retract_button.draw_button()    #绘制悔棋按钮
        replay_button.draw_button()     #绘制重玩按钮
        pygame.display.update()     #更新屏幕
        
run_game()
