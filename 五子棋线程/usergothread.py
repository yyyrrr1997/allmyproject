
import threading
class UserGoThread(threading.Thread):
    def __init__(self,engine,chessmanUser):
        super().__init__()
        self.engine =engine
        self.chessmanUser =chessmanUser
    def run(self):
        print('UserGoThread run启动')
        while True:
            userInput = input('请输入下棋坐标：')
            self.engine.parseUserInputStr(userInput,self.chessmanUser)
            self.chessmanUser.doNotify()
            self.chessmanUser.doWait()