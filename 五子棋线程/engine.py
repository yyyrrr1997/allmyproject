from chessman import *
from chessboard import *
import random

class Engine(object):
    ''' 引擎类 实现下棋的策略的规则 '''
    def __init__(self, chessboard):
        ''' 初始化方法 参数：棋盘对象 '''
        if not isinstance(chessboard, ChessBoard):
            raise Exception('参数必须为ChessBoard对象')
        self.__chessboard = chessboard

    def computerGo(self, chessman):
        ''' 电脑下棋的策略 告诉棋子的颜色 返回下棋的位置 传入chessman对象的时候 把棋子的颜色写入 在该方法中负责填写棋子的位置 '''
        if not isinstance(chessman, ChessMan):
            raise Exception('参数必须为ChessMan对象')
        while True:
            posX = random.randint(1,15)
            # 在1~15之间随机生成一个整数
            posY = random.randint(1, 15)
            # 判断随机生成的坐标是否为空 如果为空 则写入chessman对象中并退出循环
            if self.__chessboard.getChess((posX, posY)) == '+':
                print('电脑下棋的位置：%d,%d' % (posX, posY))
                # 把posX和posY写入chessman对象中
                chessman.setPos((posX, posY))
                break

    def parseUserInputStr(self, inputStr, chessman):
        ''' 用户在终端下棋
        提示用户
        传入用户输入的字符串
        解释该字符串对应的位置
        传入chessman对象的时候
        把棋子的颜色写入
        在该方法中负责填写棋子的位置
            比如用户输入3,b 则表示第3行第2列
            后续需要修改为正则表达式查询内容 '''

        if not isinstance(chessman, ChessMan):
            raise Exception('第2个参数必须为ChessMan对象')
        ret = inputStr.split(',')
        value1 = ret[0]
        value2 = ret[1]
        # 转换成坐标
        posX = int(value1)
        try:
            posY = int(value2)
        except:
            posY = ord(value2) - ord('a') + 1
        chessman.setPos((posX, posY))

    def isWon(self, pos, color):
        ''' 判断是否赢棋 当在pos位置上放置color颜色的棋子后 是否胜负已分 返回True表示胜负已分 返回False表示胜负未分 '''

        if not isinstance(pos, tuple):
            raise Exception('第1个参数必须为元组')
        if pos[0] <= 0 or pos[0] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')
        if pos[1] <= 0 or pos[1] > ChessBoard.BOARD_SIZE:
            raise Exception( '下标越界')
        # 垂直方向----------------------------------------
        startX = 1#默认第一行开始算
        if pos[0] - 4 >= 1:
            startX = pos[0] - 4 #得到的坐标往上数4 颗开始算
        endX = ChessBoard.BOARD_SIZE
        if pos[0] + 4 < ChessBoard.BOARD_SIZE:
            endX = pos[0] + 4 #得到的坐标往下数4 颗为止
        count = 0 # 统计有多少连续的棋子
        for posX in range(startX, endX + 1):
            if self.__chessboard.getChess((posX, pos[1])) == color:
                count += 1
                if count >= 5:
                    return True
            else:
                # 一旦断开 统计计数马上清0 但不能退出
                count = 0
        # 水平方向------------------------------------------
        startY = 1 #默认第一列开始算
        if pos[1] - 4 >= 1:
            startY = pos[1] - 4 #得到的坐标往左数4 颗开始算
        endY = ChessBoard.BOARD_SIZE #默认最后一列结束
        if pos[1] + 4 < ChessBoard.BOARD_SIZE:
            endY = pos[1] + 4
        #count = 0  # 统计有多少连续的棋子
        for posY in range(startY, endY + 1): #endY 要算，所以endY+1）
            if self.__chessboard.getChess((pos[0], posY)) == color:
                count += 1
                if count >= 5:
                    return True
            else:
                # 一旦断开 统计计数马上清0 但不能退出
                count = 0
        #  左上右下方向-----------------------------------------
        #count = 0  # 统计有多少连续的棋子
        sX =pos[0]-1 #x距离
        sY=pos[1]-1 #y距离
        num =min(sX,sY)
        startX =pos[0] -num #固定列数，后面变化行数
        startY = pos[1] - num#固定行数，后面变化列数
        if pos[0] - 4 >= 1 and pos[1] - 4 >= 1:
            startX = pos[0] - 4  # 得到的坐标往上数4 颗开始算
            startY = pos[1] - 4  # 得到的坐标往左数4 颗开始算
        eX = ChessBoard.BOARD_SIZE-pos[0] #x到下边界距离
        eY =ChessBoard.BOARD_SIZE-pos[1]#y到右边界距离
        num2=min(eX,eY)
        endX =pos[0] +num2
        endY =pos[1] + num2
        if pos[1] + 4 < ChessBoard.BOARD_SIZE and pos[0] + 4 < ChessBoard.BOARD_SIZE:
            endX = pos[0] + 4
            endY = pos[1] + 4
        lenY =abs(endY-startY)
        lenX =abs(endX-startX)
        leng =min(lenY,lenX)
        for i in range(0, leng+1):  # leng要算，所以leng+1）
            if self.__chessboard.getChess((startX+i, startY+i)) == color:
                count += 1
                if count >= 5:
                    return True
            else:
                # 一旦断开 统计计数马上清0 但不能退出
                count = 0
        #  左下右上方向----------------------------------
        # count = 0  # 统计有多少连续的棋子
        sX = pos[0] - 1  # x距离
        sY = ChessBoard.BOARD_SIZE-pos[1]   # y坐标到右边界的距离
        num = min(sX, sY)
        startX = pos[0] - num  # 固定列数，后面变化行数
        startY = pos[1] + num  # 固定行数，后面变化列数
        if pos[0] - 4 >= 1 and pos[1] + 4 < ChessBoard.BOARD_SIZE:
            startX = pos[0] - 4  # 得到的坐标往上数4 颗开始算
            startY = pos[1] + 4  # 得到的坐标往右数4 颗开始算
        eX = ChessBoard.BOARD_SIZE - pos[0]  # x到下边界距离
        eY = pos[1]-1  # y到左边界距离
        num2 = min(eX, eY)
        endX = pos[0] + num2
        endY = pos[1] - num2
        if pos[0] + 4 < ChessBoard.BOARD_SIZE and pos[1] - 4 >=1:
            endX = pos[0] + 4
            endY = pos[1] - 4
        lenY = abs(endY - startY)
        lenX = abs(endX - startX)
        leng = min(lenY, lenX)

        for i in range(0, leng + 1):  # leng要算，所以leng+1）
            if self.__chessboard.getChess((startX + i, startY - i)) == color:
                count += 1
                if count >= 5:
                    return True
            else:
                # 一旦断开 统计计数马上清0 但不能退出
                count = 0
        return False

