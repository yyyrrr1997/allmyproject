#-*- coding:utf-8 -*-
import socket
import threading
import re
# 子线程类
class ClientThread(threading.Thread):
    def __init__(self, clientSocket):
        super().__init__()
        self.clientSocket = clientSocket
    def run(self):
        try:
            while True:
                # 接收信息
                recvData = self.clientSocket.recv(1024)
                recvData=recvData.decode('gbk')
                print('收到服务端发送过来的信息：%s' % recvData)

                pattern = '请输入'
                result =re.search(pattern,recvData)
                if result!=None:

                    # 要发送的信息
                    msg = input('请输入：')
                    print('往服务端发送消息：%s' % msg)
                    self.clientSocket.send(msg.encode('gbk'))


        except:
            pass
        finally:
            print('客户端退出连接' )
if __name__ == '__main__':
    clientSocket = None
    try:
        print('启动客户端')
        # 创建流式套接字(TCP)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 服务端地址
        serverAddress = '192.168.101.57'
        serverPort = 8888
        print('连接服务端的地址为%s, 端口号为%d' % (serverAddress, serverPort))
        serverInfo = (serverAddress, serverPort)
        clientSocket.connect(serverInfo)
        # 创建子线程并启动
        t = ClientThread(clientSocket)
        # 设置子线程为守护线程
        t.setDaemon(True)
        # 启动子线程
        t.start()
        # 等待子线程的退出
        t.join()
    except:
        print('连接服务器失败')
    finally:
        # 关闭socket
        print('关闭客户端')
        clientSocket.close()