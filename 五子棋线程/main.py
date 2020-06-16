#-*- coding:utf-8 -*-
from chessboard import *
from engine import  *
from usergothread import *
from computergothread import *

def mainThread():
    '''多线程五子棋的主流程'''
    # 创建棋盘并初始化
    chessboard = ChessBoard()
    chessboard.initBoard()
    chessboard.printBoard()
    # 创建引擎对象（棋局规则）
    engine = Engine(chessboard)
    # 创建两个棋手
    chessmanUser = ChessMan()
    chessmanUser.setColor('x')# 用户执黑
    chessmanPC = ChessMan()
    chessmanPC.setColor('o') # 电脑执白
    #  启动两个线程（棋手的下棋策略=脑子）
    computerGo = ComputerGoThread(engine, chessmanPC)
    usergo = UserGoThread(engine, chessmanUser)
    computerGo.setDaemon(True)
    usergo.setDaemon(True)
    computerGo.start()
    usergo.start()
    # 开始循环
    while True:#（图像交互）

        chessmanUser.doWait()# 1. 等待用户线程notify
        # 2. 在棋盘上摆放棋子
        chessboard.setChessMan(chessmanUser)
        #判断
        pos = chessmanUser.getPos()
        if engine.isWon(pos, 'x'):
            chessboard.printBoard()
            print('恭喜赢了')
            break

        chessmanPC.doNotify()# 3. 通知电脑线程 finish wait
        chessmanPC.doWait()# 4. 等待电脑线程notify
        # 5. 在棋盘上摆放棋子
        chessboard.setChessMan(chessmanPC)
        chessboard.printBoard()
        # 判断
        pos = chessmanPC.getPos()
        if engine.isWon(pos, 'o'):
            print('呵呵输了')
            break

        chessmanUser.doNotify() # 6. 通知用户线程finish wait

if __name__ == '__main__':
    mainThread()
