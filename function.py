# encoding:utf-8
import pygame
import sys
import pygame.font
import winsound     #用作播放点击错误的声音
from random import choice

import chess
import settings as st

def check_keydown(chess,bigchess,windows, screen, st, retract_button, replay_button):
    '''检测按键'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if st.game_active:
                check_position(mouse_x, mouse_y, chess,bigchess, st)
            stop(chess,bigchess,st)
            check_button(screen, retract_button, replay_button,windows,
                         chess,bigchess,st, mouse_x, mouse_y)

def check_position(mouse_x, mouse_y, chess,bigchess, st):
    '''产生点击的坐标'''
    a = ''
    position1 = ''
    position2 = []
    if st.center_x - 142.5 <= mouse_x <= st.center_x - 52.5:  # 大第一列
        a += '1'
    elif st.center_x - 45 <= mouse_x <= st.center_x + 45:  # 大第二列
        a += '2'
    elif st.center_x + 52.5 <= mouse_x <= st.center_x + 142.5:  # 大第三列
        a += '3'

    if st.center_y - 142.5 <= mouse_y <= st.center_y - 52.5:  # 大第一行
        a += '4'
    elif st.center_y - 45 <= mouse_y <= st.center_y + 45:  # 大第二行
        a += '5'
    elif st.center_y + 52.5 <= mouse_y <= st.center_y + 142.5:  # 大第三行
        a += '6'

    if len(a) > 1:
        '''小九宫行列对应'''  # a[0]为列数 a[1]为行数    position1记录该格子在81个格子内的坐标
        if a[0] == '1':
            if st.center_x - 142.5 <= mouse_x <= st.center_x - 113.5:
                position1 += '1'
                position2.append(st.center_x - 142)
            elif st.center_x - 112 <= mouse_x <= st.center_x - 83:
                position1 += '2'
                position2.append(st.center_x - 111.5)
            elif st.center_x - 81.5 <= mouse_x <= st.center_x - 52.5:
                position1 += '3'
                position2.append(st.center_x - 81)

        elif a[0] == '2':
            if st.center_x - 45 <= mouse_x <= st.center_x - 16:
                position1 += '4'
                position2.append(st.center_x - 44.5)
            elif st.center_x - 14.5 <= mouse_x <= st.center_x + 14.5:
                position1 += '5'
                position2.append(st.center_x - 14)
            elif st.center_x + 16 <= mouse_x <= st.center_x + 45:
                position1 += '6'
                position2.append(st.center_x + 16.5)

        elif a[0] == '3':
            if st.center_x + 52.5 <= mouse_x <= st.center_x + 81.5:
                position1 += '7'
                position2.append(st.center_x + 53)
            elif st.center_x + 83 <= mouse_x <= st.center_x + 112:
                position1 += '8'
                position2.append(st.center_x + 83.5)
            elif st.center_x + 113.5 <= mouse_x <= st.center_x + 142.5:
                position1 += '9'
                position2.append(st.center_x + 114)
        if a[1] == '4':
            if st.center_y - 142.5 <= mouse_y <= st.center_y - 113.5:
                position1 += '1'
                position2.append(st.center_y - 142)
            elif st.center_y - 112 <= mouse_y <= st.center_y - 83:
                position1 += '2'
                position2.append(st.center_y - 111.5)
            elif st.center_y - 81.5 <= mouse_y <= st.center_y - 52.5:
                position1 += '3'
                position2.append(st.center_y - 81)

        elif a[1] == '5':
            if st.center_y - 45 <= mouse_y <= st.center_y - 16:
                position1 += '4'
                position2.append(st.center_y - 44.5)
            elif st.center_y - 14.5 <= mouse_y <= st.center_y + 14.5:
                position1 += '5'
                position2.append(st.center_y - 14)
            elif st.center_y + 16 <= mouse_y <= st.center_y + 45:
                position1 += '6'
                position2.append(st.center_y + 16.5)

        elif a[1] == '6':
            if st.center_y + 52.5 <= mouse_y <= st.center_y + 81.5:
                position1 += '7'
                position2.append(st.center_y + 53)
            elif st.center_y + 83 <= mouse_y <= st.center_y + 112:
                position1 += '8'
                position2.append(st.center_y + 83.5)
            elif st.center_y + 113.5 <= mouse_y <= st.center_y + 142.5:
                position1 += '9'
                position2.append(st.center_y + 114)

        if len(position1) > 1 and len(position2) > 1:
            chess.save(bigchess,position1, position2)
            bigchess.check_big_chess(chess)

def check_button(screen,retract_button,replay_button,windows,chess,bigchess,st,mouse_x, mouse_y):
    '''检查是否点击按钮'''
    if retract_button.rect.collidepoint(mouse_x, mouse_y):
        if not st.active_windows:
            chess.retract()
            bigchess.check_big_chess(chess)
            st.game_active = True; st.win = -1
            winsound.PlaySound("materials/button.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)       #异步播放点击按按钮的音乐
    elif replay_button.rect.collidepoint(mouse_x, mouse_y):
        if not st.active_windows:
            st.active_windows = True
            st.game_active = False
            winsound.PlaySound("materials/button.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)       #异步播放点击按按钮的音乐
    elif windows.msg2_button.rect.collidepoint(mouse_x, mouse_y):
        if st.active_windows:
            st.game_active = True
            st.active_windows = False
            chess.O1.clear()
            chess.O2.clear()
            chess.X1.clear()
            chess.X2.clear()
            bigchess.check_big_chess(chess)
            winsound.PlaySound("materials/button.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)       #异步播放点击按按钮的音乐
    elif windows.msg3_button.rect.collidepoint(mouse_x, mouse_y):
        if st.active_windows:
            st.game_active = True
            st.active_windows = False
            stop(chess,bigchess,st)
            winsound.PlaySound("materials/button.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)       #异步播放点击按按钮的音乐

def draw(chess,bigchess, screen,windows, st):
    '''绘制图形'''
    imageX = pygame.image.load('materials/X.bmp')
    imageO = pygame.image.load('materials/O.bmp')
    imageXr = pygame.image.load('materials/Xr.bmp')
    imageOr = pygame.image.load('materials/Or.bmp')
    imageBigX = pygame.image.load('materials/bigX.bmp')
    imageBigO = pygame.image.load('materials/bigO.bmp')
    image_frame = pygame.image.load('materials/frame.gif')
    image_big_frame = pygame.image.load('materials/big_frame.gif')

    # 绘制普通棋子
    for position2 in chess.O2:
        screen.blit(imageO,(position2[0], position2[1]))
    for position2 in chess.X2:
        screen.blit(imageX,(position2[0], position2[1]))

    # 绘制最后一颗棋子
    if len(chess.X1) > len(chess.O1):
        screen.blit(imageXr,(chess.X2[-1][0], chess.X2[-1][1]))
    elif len(chess.X1) == len(chess.O1) and len(chess.X1) > 0:
        screen.blit(imageOr,(chess.O2[-1][0], chess.O2[-1][1]))
        
    #绘制大棋
    for u in bigchess.bigX:
        x = st.top_left_corner[0]+7.5+(u[0]-1)*97.5
        y = st.top_left_corner[1]+7.5+(u[1]-1)*97.5
        screen.blit(imageBigX,(x,y))
    for u in bigchess.bigO:
        x = st.top_left_corner[0]+7.5+(u[0]-1)*97.5
        y = st.top_left_corner[1]+7.5+(u[1]-1)*97.5
        screen.blit(imageBigO,(x,y))

    #绘制下棋区域
    last_position = ''  # 上一个棋的位置，若无，则空
    if len(chess.X1) > len(chess.O1):
        last_position = chess.X1[-1]
    elif len(chess.X1) == len(chess.O1) and len(chess.X1) > 0:
        last_position = chess.O1[-1]
    if last_position:
        x = (int(last_position[0]) - 1) % 3 + 1  # x,y为上一个棋对应的宫的相对位置
        y = (int(last_position[1]) - 1) % 3 + 1
        if [x,y] in bigchess.bigX or [x,y] in bigchess.bigO:
            screen.blit(image_big_frame, (st.top_left_corner[0], st.top_left_corner[1]))
        else:
            x_position = st.top_left_corner[0] + (x - 1) * 97.5  # 这两个变量为绘制的框的绝对位置
            y_position = st.top_left_corner[1] + (y - 1) * 97.5  # 97.5为棋盘的宫的宽度加上粗边的宽度
            screen.blit(image_frame, (x_position, y_position))
    else:
        screen.blit(image_big_frame, (st.top_left_corner[0], st.top_left_corner[1]))
        
    #显示输赢的文字
    def draw_text(text,text_color,font,st,screen):
        textobj = font.render(text,True,text_color,st.bg_color)
        text_rect = textobj.get_rect()
        text_rect.center = center
        screen.blit(textobj,text_rect)
    if st.win>=0:
        font = pygame.font.SysFont(None, 60)
        text_color = (255, 255, 255)
        center = (250,190)
        if st.win==0:draw_text('Draw!',text_color,font,st,screen)
        elif st.win==1:draw_text('X wins!',text_color,font,st,screen)
        elif st.win==2:draw_text('O wins!',text_color,font,st,screen)
        
    #绘制重新开始提示界面
    if st.active_windows:
        windows.draw_windows()

def stop(chess,bigchess,st):
    '''判断游戏是否结束'''
    def find(u):
        '''判断大棋是否连成一条线'''
        if [2,2] in u:
            if [1,1] in u and [3,3] in u:return True
            if [3,1] in u and [1,3] in u:return True
            if [1,2] in u and [3,2] in u:return True
            if [2,1] in u and [2,3] in u:return True
        if [1,1] in u:
            if [2,1] in u and [3,1] in u:return True
            if [1,2] in u and [1,3] in u:return True
        if [3,3] in u:
            if [3,1] in u and [3,2] in u:return True
            if [1,3] in u and [2,3] in u:return True
        return False
    if find(bigchess.bigX):
        st.game_active = False
        st.win = 1
    elif find(bigchess.bigO):
        st.game_active = False
        st.win = 2
    else:
        if len(bigchess.bigX)+len(bigchess.bigO)==9:
            st.win = 0
            st.game_active = False
        else:
            num = [0 for i in range(9)]  #存放每个小九宫格内的棋子数量，若被大棋占领，则为9
            flag = [False for i in range(9)]    #是否被大棋占领
            for i in bigchess.bigX:num[(i[1]-1)*3+i[0]-1]=9;flag[(i[1]-1)*3+i[0]-1]=True
            for i in bigchess.bigO:num[(i[1]-1)*3+i[0]-1]=9;flag[(i[1]-1)*3+i[0]-1]=True
            for i in chess.X1:
                x = (int(i[0])-1)//3+1; y = (int(i[1])-1)//3+1
                if not flag[(y-1)*3+x-1]:num[(y-1)*3+x-1]+=1
            for i in chess.O1:
                x = (int(i[0])-1)//3+1; y = (int(i[1])-1)//3+1
                if not flag[(y-1)*3+x-1]:num[(y-1)*3+x-1]+=1
            if sum(num)==81:
                st.win = 0
                st.game_active = False
            else:
                st.win = -1
                game_active = True
    
# def ai(chess,bigchess,st):
    # pos = [[str(x),str(y)] for x in range(1,10) for y in range(1,10)]
    # if len(chess.X1)>len(chess.O1) and st.game_active:
        # position1 = choice(pos)
        # position1 = ''.join(position1)
        # position2 = []
        # if position1[0]=='1':position2.append(st.center_x - 142)
        # elif position1[0]=='2':position2.append(st.center_x - 111.5)
        # elif position1[0]=='3':position2.append(st.center_x - 81)
        # elif position1[0]=='4':position2.append(st.center_x - 44.5)
        # elif position1[0]=='5':position2.append(st.center_x - 14)
        # elif position1[0]=='6':position2.append(st.center_x + 16.5)
        # elif position1[0]=='7':position2.append(st.center_x + 53)
        # elif position1[0]=='8':position2.append(st.center_x + 83.5)
        # elif position1[0]=='9':position2.append(st.center_x + 114)
        # if position1[1]=='1':position2.append(st.center_y - 142)
        # elif position1[1]=='2':position2.append(st.center_y - 111.5)
        # elif position1[1]=='3':position2.append(st.center_y - 81)
        # elif position1[1]=='4':position2.append(st.center_y - 44.5)
        # elif position1[1]=='5':position2.append(st.center_y - 14)
        # elif position1[1]=='6':position2.append(st.center_y + 16.5)
        # elif position1[1]=='7':position2.append(st.center_y + 53)
        # elif position1[1]=='8':position2.append(st.center_y + 83.5)
        # elif position1[1]=='9':position2.append(st.center_y + 114)
        # chess.save(bigchess,position1, position2)
        # bigchess.check_big_chess(chess)
    






