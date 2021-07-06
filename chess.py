# encoding:utf-8
import pygame
import winsound     #用作播放点击错误的声音

class Chess():
    def __init__(self):
        self.O1 = []  # 1为相对坐标，从左上角'11'到'右下角'99'，第一个数是横坐标
        self.O2 = []  # 2为绝对坐标
        self.X1 = []
        self.X2 = []

    def save(self, bigchess, position1, position2):
        '''保存坐标'''
        if position1 not in self.X1 and position1 not in self.O1:       #判断是否落在之前下过的地方
            if self.check_chess_position(bigchess,position1):           #判断是否落在应该下的地方
                if len(self.X1) > len(self.O1):                #判断该次所下的子为哪方所下
                    self.O1.append(position1)                  #将该次所下的子的坐标存入列表
                    self.O2.append(position2)
                else:
                    self.X1.append(position1)
                    self.X2.append(position2)
                winsound.PlaySound("materials/chess.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)        #异步播放点击落子的音乐
            else:
                winsound.PlaySound("materials/Wrong.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)          #异步播放点击错误的音乐
        else:
            winsound.PlaySound("materials/Wrong.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    def retract(self):
        if len(self.X1) > len(self.O1):
            self.X1.pop()
            self.X2.pop()
        elif len(self.X1) == len(self.O1) and len(self.X1) > 0:
            self.O1.pop()
            self.O2.pop()

    def isfull(self, bigchess, x, y):
        '''判断某个宫是否被大棋占领或者已满'''
        if [x,y] in bigchess.bigX or [x,y] in bigchess.bigO:
            return True
        cnt = 0
        for i in range(3*x-2,3*x+1):
            for j in range(2*y+1,2*y+4):
                if str(i)+str(j) in self.X1 or str(i)+str(j) in self.O1:
                    cnt += 1
        if cnt==9: 
            return True
        return False
    
    def check_chess_position(self, bigchess, position1):
        '''检验棋子是否落入正确区域'''
        flag = False  # 若是，则flag=True
        last_position = ''  # 上一个棋的位置，若无，则空
        if len(self.X1) > len(self.O1):
            last_position = self.X1[-1]
        elif len(self.X1) == len(self.O1) and len(self.X1) > 0:
            last_position = self.O1[-1]
        if not last_position:   #如果这是第一步棋，那下哪里都可以
            flag = True
        else:
            x = (int(last_position[0]) - 1) % 3 + 1  # x,y为上一个棋对应的宫的相对位置，这一步棋应该下在这里
            y = (int(last_position[1]) - 1) % 3 + 1
            if self.isfull(bigchess, x, y):    #判断[x,y]这个位置是否被大棋占领或已满
                #如果已满则下在哪里都可以，除了被大棋占领的地方
                x_ = (int(position1[0])-1)//3+1     #x_,y_为这次落子的宫的相对坐标
                y_ = (int(position1[1])-1)//3+1
                if [x_,y_] in bigchess.bigX or [x_,y_] in bigchess.bigO:    #如果这个位置已被大棋占领，则位置不正确
                    flag=False
                else:
                    flag=True
            elif x == ((int(position1[0]) - 1) // 3 + 1) and y == ((int(position1[1]) - 1) // 3 + 1):
                #否则要下在该下的地方
                flag = True
        return flag


class BigChess():
    def __init__(self):
        self.bigO = []  #大棋的相对坐标，从左上角[1,1]到右下角[3,3]，第一个数是横坐标
        self.bigX = []

    def check_big_chess(self,chess):
        def transform(u):
            '''将[x,y]变换为(1,1)至(3,3)内'''
            while u[0]>3:u[0]-=3
            while u[1]>3:u[1]-=3
            return u
        def findbig(u):
            '''判断小棋是否连成一条线'''
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
        #xh(n)为第n行，每一项的第n个（从1开始）为第n列
        xh1=[[] for i in range(3)];xh2=[[] for i in range(3)];xh3=[[] for i in range(3)]
        oh1=[[] for i in range(3)];oh2=[[] for i in range(3)];oh3=[[] for i in range(3)]
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
