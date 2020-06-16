import socket
import threading
import time
from chessboard import *
from engine import  *


class boardThread(threading.Thread):
    def __init__(self,clientSocket,clientInfo):
        super().__init__()
        self.clientSocket=clientSocket
        self.clientInfo =clientInfo

        print('等待第二位客人连接')
        self.clientSocket2, self.clientInfo2 = serverSocket.accept()
        self.turn = 1
        global clients
        clients += 1

    def run(self):
        try:
            while True:
                print('游戏开始')
                self.initboard()
                print('棋盘初始化成功')
                # 接收信息
                while True:
                    if self.turn %2 != 0:
                        goSocket = self.clientSocket
                        waitSocket=self.clientSocket2
                        man =self.member1
                    else:
                        goSocket = self.clientSocket2
                        waitSocket = self.clientSocket
                        man = self.member2
                    msg = '请输入下棋坐标'
                    goSocket.send(msg.encode('gbk'))
                    msg2='等待对方落子'
                    waitSocket.send(msg2.encode('gbk'))
                    recvData = goSocket.recv(1024)
                    recvData=recvData.decode('gbk')
                    if recvData!='':
                        print('%s:客户端发送过来的信息为：%s' % (self.name,recvData))
                        #在棋盘落子
                        self.engine.parseUserInputStr(recvData, man)
                        self.chessboard.setChessMan(man)
                        self.chessboard.printBoard()
                        #判断棋局
                        pos = man.getPos()
                        color =man.getColor()
                        if self.engine.isWon(pos, color):
                            self.chessboard.printBoard()
                            msg='恭喜赢了'
                            goSocket.send(msg.encode('gbk'))
                            msg2 = '输了，再接再厉'
                            waitSocket.send(msg2.encode('gbk'))
                            break
                        self.turn+=1
                msg='棋局结束。双方准备则开新局 请输入：y=准备 / n=退出：'
                goSocket.send(msg.encode('gbk'))
                waitSocket.send(msg.encode('gbk'))
                recvData1 = goSocket.recv(1024)
                recvData2 = waitSocket.recv(1024)
                if recvData1==recvData2 =='y':
                    continue
                else :
                    break


        except:
            pass
        finally:
            print('客户端退出连接，线程%s结束'%self.name)

    def initboard(self):
        '''五子棋的主流程'''
        # 创建棋盘并初始化
        self.chessboard = ChessBoard()
        self.chessboard.initBoard()
        self.chessboard.printBoard()
        # 创建引擎对象（棋局规则）
        self.engine = Engine(self.chessboard)
        # 创建两个棋手
        self.member1 = ChessMan()
        self.member1.setColor('x')  # 用户1执黑
        self.member2 = ChessMan()
        self.member2.setColor('o')  # 用户2执白

if __name__=='__main__':

    try:
        clients = 0
        print('启动服务器')
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        # 绑定服务端
        serverAddress = ''  # 取默认
        serverPort = 8888
        serverInfo = (serverAddress, serverPort)
        serverSocket.bind(serverInfo)
        print('绑定服务器，端口号为%s'%serverPort )
        # listen监听
        serverSocket.listen(5)
        print('等待客户端连接')
        while True:
            clientSocket, clientInfo = serverSocket.accept()
            clients+=1
            if clients%2!=0:
                print('启动新棋盘')
                serverboard =boardThread(clientSocket,clientInfo)
                serverboard.setDaemon(True)
                serverboard.start()




    except Exception as e:
        print(e)
    finally:
        # 关闭socket
        print('关闭服务端')
        serverSocket.close()