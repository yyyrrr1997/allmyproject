from chessman import *
class ChessBoard(object):
    '''棋盘类'''
    BOARD_SIZE = 15 # 棋盘大小
    def __init__(self):
        '''初始化方法'''
        # 棋盘索引从(0,0)~(15,15)
        '''self.__board = [[0 for i in range(0, ChessBoard.BOARD_SIZE + 1)] for j in range(0,ChessBoard.BOARD_SIZE + 1)]
        '''
        self.__board = []
        # 二维坐标
        for i in range(0, ChessBoard.BOARD_SIZE + 1):
            line = []
            # 一维坐标 表示棋盘上的一行
            for j in range(0, ChessBoard.BOARD_SIZE + 1):
                line.append(0)
            # 一个坐标点
            self.__board.append(line)

    def initBoard(self):
        '''清空棋盘'''
        # 把所有坐标点都设置为'+'
        #  直接忽略第0行
        for i in range(1, ChessBoard.BOARD_SIZE + 1): # [1,16)  即下标1到下标15
            for j in range(1, ChessBoard.BOARD_SIZE + 1):  # [1, 16)
                self.__board[i][j] = '+'

    def printBoard(self):
        '''打印棋盘'''
        # 打印列号
        print('   ', end = '') #列号对齐棋盘
        for i in range(1, ChessBoard.BOARD_SIZE + 1): # [1,16)
            #  ord() :字符转ASCII码值
            #  chr() :ASCII码值转字符
            c = chr(ord('a') + i - 1)
            print(c, end = '')
        print()# 第一行列号打印结束，换行
        # 打印行号和棋盘
        for i in range(1, ChessBoard.BOARD_SIZE + 1): # [1,16)
            #  打印行号
            if 1 <= i <= 9:
                print(' ', end = '') # 打印一个空格方便对齐个位数和十位数
            print(i, end = ' ') #打印行号
                # 打印棋盘
            for j in range(1, ChessBoard.BOARD_SIZE + 1): # [1, 16)
                print(self.__board[i][j], end = '') # 不换行
            print() # 第j行打印结束，换行

    def setChess(self, pos, color):
        '''在指定位置放置指定颜色棋子
        参数1pos 坐标 必须为元组 长度为2
        参数2color 棋子的颜色 必须为'x'或'o' '''
        if not isinstance(pos, tuple): #判断pos是否为tuple的对象。如果坐标不是为元组
            raise Exception('第一个参数请输入正确的坐标格式：（x,y）')
        if pos[0] <= 0 or pos[0] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')
        if pos[1] <= 0 or pos[1] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')
        self.__board[pos[0]][pos[1]] = color

    def setChessMan(self, chessman):
        ''' 把chessman对象放置到棋盘上 参数: 棋子对象 必须为ChessMan对象 '''

        if not isinstance(chessman, ChessMan):#p判断chessman是否为ChessMan的对象
            raise Exception('第1个参数必须为ChessMan对象')
        pos = chessman.getPos()
        color = chessman.getColor()
        self.setChess(pos, color)

    def getChess(self, pos):
        '''得到坐标位置'''
        if not isinstance(pos, tuple):
            raise Exception('第1个参数必须为元组')
        if pos[0] <= 0 or pos[0] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')
        if pos[1] <= 0 or pos[1] > ChessBoard.BOARD_SIZE:
            raise Exception('下标越界')

        return self.__board[pos[0]][pos[1]]

    def isEmpty(self, pos):
        '''判断坐标是否为空'''
        if not isinstance(pos, tuple): raise Exception('第1个参数必须为元组')
        if pos[0] <= 0 or pos[0] > ChessBoard.BOARD_SIZE: raise Exception('下标越界')
        if pos[1] <= 0 or pos[1] > ChessBoard.BOARD_SIZE: raise Exception('下标越界')
        if self.__board[pos[0]][pos[1]] == 'x':
            return False
        elif self.__board[pos[0]][pos[1]] == 'o':
            return False
        return True


