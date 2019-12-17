
TicTacToe
=
一种进阶版的井字棋。

基于pygame开发，运行前需安装pygame，然后直接双击TicTacToe.py就可以运行。


**规则：**

1.双人对战，分为O方和X方，X方先下，O方后下，轮流下棋。

1.棋盘类似数独，将9乘9的棋盘划分为9个3乘3的宫，玩家只能在小格子里面下棋

2.每个宫内，只要任意一方横着或者竖着或者对角线连成一条直线，那么这个宫就自动合成一个大的棋子。

3.把每一个宫看成一格，只要任意一方的大棋横着或者竖着或者对角线连成一条直线，那么这一方获胜,概括而言同井字棋。

4.下棋区域限定：当对方下了一步棋之后，本方玩家必须将自己的棋下在对方上一步下的棋所在的小九宫格对应位置的大九宫格里面。若这个大九宫格已经被大棋所占领，那么本方可以下在九宫格内任意空白的位置。

**更新:**
___
*v1.0 完成下棋部分*   
*v1.1完成反馈音乐之错误点击*
___


#### 目前已实现功能：

1.绘制画图区域。

2.可以在九宫格内下棋，能识别鼠标点击区域。

3.限制下棋区域。

4.用红色标出上一步下的棋。

5.悔棋和重玩功能。
___
#### 未来计划：

1.能检测和绘制大棋。

2.判定胜负。

3.能让玩家自由设置背景颜色。

4.添加开始游戏和设置界面。

5.实现网络对战。

6.实现人机对战。

7.重新编辑README.md。
