# encoding:utf-8
import pygame
import winsound     #用作播放点击错误的声音

class Chess():
    def __init__(self):
        self.O1 = []  # 1为相对坐标
        self.O2 = []  # 2为绝对坐标
        self.X1 = []
        self.X2 = []

    def save(self,bigchess, position1, position2):
        '''保存坐标'''
        if position1 not in self.X1 and position1 not in self.O1:       #判断是否落在之前下过的地方
            if self.check_chess_position(bigchess,position1):           #判断是否落在应该下的地方
                if len(self.X1) > len(self.O1):                #判断该次所下的子为哪方所下
                    self.O1.append(position1)                  #将该次所下的子的坐标存入列表
                    self.O2.append(position2)
                else:
                    self.X1.append(position1)
                    self.X2.append(position2)
            else:
                winsound.PlaySound("images/Wrong.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)          #异步播放点击错误的音乐
        else:
            winsound.PlaySound("images/Wrong.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    def retract(self):
        if len(self.X1) > len(self.O1):
            self.X1.pop()
            self.X2.pop()
        elif len(self.X1) == len(self.O1) and len(self.X1) > 0:
            self.O1.pop()
            self.O2.pop()

    def check_chess_position(self,bigchess, position1):
        '''检验棋子是否落入正确区域'''
        flag = False  # 若是，则flag=True
        last_position = ''  # 上一个棋的位置，若无，则空
        if len(self.X1) > len(self.O1):
            last_position = self.X1[-1]
        elif len(self.X1) == len(self.O1) and len(self.X1) > 0:
            last_position = self.O1[-1]
        if last_position:
            x = (int(last_position[0]) - 1) % 3 + 1  # x,y为上一个棋对应的宫的相对位置
            y = (int(last_position[1]) - 1) % 3 + 1
            if [x,y] in bigchess.bigX or [x,y] in bigchess.bigO:flag=True
            elif x == ((int(position1[0]) - 1) // 3 + 1) and y == ((int(position1[1]) - 1) // 3 + 1):
                flag = True
        else:
            flag = True
        return flag


class BigChess():
    def __init__(self):
        self.bigO = []
        self.bigX = []

    def check_big_chess(self,chess):
        def transform(u):
            '''将[x,y]变换为(1,1)至(3,3)内'''
            while u[0]>3:u[0]-=3
            while u[1]>3:u[1]-=3
            return u
        def findbig(u):
            '''查找大棋'''
            if [2,2] in u:
                if [1,1] in u and [3,3] in u:return True
                elif [3,1] in u and [1,3] in u:return True
                elif [1,2] in u and [3,2] in u:return True
                elif [2,1] in u and [2,3] in u:return True
            elif [1,1] in u:
                if [2,1] in u and [3,1] in u:return True
                elif [1,2] in u and [1,3] in u:return True
            elif [3,3] in u:
                if [3,1] in u and [3,2] in u:return True
                elif [1,3] in u and [2,3] in u:return True
            return False
        #xh(n)为第n行，每一项的第n个（从1开始）为第n列
        xh1=[[] for i in range(3)];xh2=[[] for i in range(3)];xh3=[[] for i in range(3)]
        oh1=[[] for i in range(9)];oh2=[[] for i in range(9)];oh3=[[] for i in range(9)]
        self.bigX = []; self.bigO = []
        for x in range(1,10):
            for y in range(1,10):
                if str(x)+str(y) in chess.X1:
                    eval('xh'+str((y-1)//3+1))[(x-1)//3].append(transform([x,y]))
                elif str(x)+str(y) in chess.O1:
                    eval('oh'+str((y-1)//3+1))[(x-1)//3].append(transform([x,y]))
        for i in range(1,4):
            for j in range(1,4):
                if findbig(eval('xh'+str(j))[i-1]):self.bigX.append([i,j])
                if findbig(eval('oh'+str(j))[i-1]):self.bigO.append([i,j])
    
    
    
    
    
